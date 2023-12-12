# Load necessary libraries
library(ggplot2)
library(jsonlite)
library(scales)

# Read JSON data from your file
json_data <- fromJSON("/Users/yuliang/Downloads/fees-usd-per-transaction.json")

# Convert to data frames
fees_data <- as.data.frame(json_data$`fees-usd-per-transaction`)
market_price_data <- as.data.frame(json_data$`market-price`)

# Convert timestamps from milliseconds to Date format
convert_date <- function(time) as.Date(as.POSIXct(as.numeric(time)/1000, origin="1970-01-01", tz = "UTC"))
fees_data$x <- convert_date(fees_data$x)
market_price_data$x <- convert_date(market_price_data$x)

# Filter data from 2014 onwards
start_date <- as.Date("2014-01-01")
fees_data <- subset(fees_data, x >= start_date)
market_price_data <- subset(market_price_data, x >= start_date)

# Determine the scale factor for the secondary axis
scale_factor <- max(market_price_data$y) / max(fees_data$y)

# Plotting the data with separate y-axes and enhanced aesthetics
p <- ggplot() +
  geom_line(data = fees_data, aes(x = x, y = y, color = "Fees (USD)"), size = 1) +
  geom_line(data = market_price_data, aes(x = x, y = y / scale_factor, color = "Market Price (USD)"), size = 1) +
  scale_y_continuous(name = "Fees (USD)", 
                     sec.axis = sec_axis(~ . * scale_factor, name = "Market Price (USD)")) +
  scale_color_manual(values = c("Fees (USD)" = "blue", "Market Price (USD)" = "red"),
                     labels = c("Fees (USD)", "Market Price (USD)")) +
  guides(color = guide_legend(title = "Legend")) +
  labs(title = "Bitcoin Transaction Fees and Market Price Over Time (2014 - Latest)", 
       subtitle = "Data from Blockchain.com", 
       x = "Date", y = "Value (USD)", caption = "Source: Blockchain.com") +
  theme_minimal(base_size = 14) +
  theme(plot.title = element_text(hjust = 0.5, size = 16),
        plot.subtitle = element_text(hjust = 0.5, size = 12),
        plot.caption = element_text(hjust = 0.5, size = 10),
        axis.text.x = element_text(angle = 45, hjust = 1),
        panel.background = element_rect(fill = "white", colour = "white"),
        legend.position = "bottom",
        legend.title = element_blank(),
        legend.text = element_text(size = 12))

# Save the plot to a file
ggsave("enhanced_plot_with_legend.png", plot = p, width = 12, height = 8)
