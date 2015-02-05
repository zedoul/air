library("devtools")
library("CausalImpact")

# data
csv_data = read.csv('./correlate-yen_exchange_rate.csv')
time.points <- as.Date(csv_data[,c(1,2)]$Date, "%Y-%m-%d")
x1 <- 1:530 # predictor
y <- csv_data$yen.exchange.rate #response variable
data <- zoo(cbind(y, x1), time.points)
pre.period <- c(1,470)
post.period <- c(471,530)
post.period.response <- y[post.period[1] : post.period[2]]
y[post.period[1] : post.period[2]] <- NA

# train bsts model
sdy <- sd(y, na.rm = TRUE)
ss <- list()
sd.prior <- SdPrior(sigma.guess = 0.01 * sdy, upper.limit=sdy, sample.size = 32)
ss <- AddLocalLevel(ss, y, sigma.prior = sd.prior)
bsts.model <- bsts(y ~ x1, 
        state.specification = ss, 
        niter = 1000, 
        ping = 0, save.prediction.errors = TRUE, seed = 1)

# causal impact with RunWithBstsModel, not with RunWithData
# so it do not need to use ConstructModel
impact <- CausalImpact(bsts.model = bsts.model, post.period.response = post.period.response)
plot(impact)
