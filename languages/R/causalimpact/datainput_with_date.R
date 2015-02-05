library("devtools")
library("CausalImpact")

# data
csv_data = read.csv('./correlate-yen_exchange_rate.csv')
time.points <- as.Date(csv_data[,c(1,2)]$Date, "%Y-%m-%d")
x1 <- 1:530 # predictor
y <- csv_data$yen.exchange.rate #response variable
data <- zoo(cbind(y, x1), time.points)

# causal impact
pre.period <- as.Date(c("2004-01-04","2012-12-30"))
post.period <- as.Date(c("2013-01-06","2014-02-23"))
impact <- CausalImpact(data, pre.period, post.period)
plot(impact)
