# Load library
library(ggplot2)

# Create dataset
data <- data.frame(
  PostID = c("P001","P002","P003","P004","P005"),
  Platform = c("Twitter","Facebook","Twitter","Instagram","Facebook"),
  Likes = c(120,95,130,160,100),
  Shares = c(45,40,50,70,30),
  Type = c("Video","Image","Text","Image","Video"),
  Date = as.Date(c("2025-06-01","2025-06-02","2025-06-03","2025-06-04","2025-06-05"))
)

# Plot
ggplot(data, aes(x = Platform, y = Likes, fill = Platform)) +
  geom_bar(stat = "identity") +
  labs(title = "Likes Across Platforms",
       x = "Platform",
       y = "Number of Likes") +
  theme_minimal()