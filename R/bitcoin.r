# ... [previous code for loading libraries, reading data, and data preparation]

# Determine the scale factor for the secondary axis
scale_factor <- max(market_price_data$y) / max(fees_data$y)

# Plotting the data with separate y-axes
p <- ggplot() +
  geom_line(data = fees_data, aes(x = x, y = y), color = "blue") +
  geom_line(data = market_price_data, aes(x = x, y = y / scale_factor), color = "red") +
  scale_y_continuous(name = "Fees (USD)", 
                     sec.axis = sec_axis(~ . * scale_factor, name = "Market Price (USD)")) +
  labs(title = "Bitcoin Transaction Fees and Market Price Over Time (2014 - Latest)", 
       x = "Date", y = "Value") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 90, hjust = 1))

# Save the plot to a file
ggsave("plot.png", width = 10, height = 6)
