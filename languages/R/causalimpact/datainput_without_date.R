library("CausalImpact")

# data
csv_data = read.csv('./correlate-yen_exchange_rate.csv')
x <- 1:530
y <- csv_data$yen.exchange.rate
data <- cbind(y, x)
pre.period <- c(1,470)
post.period <- c(471,530)

# causal impact
impact <- CausalImpact(data, pre.period, post.period)
plot(impact)
