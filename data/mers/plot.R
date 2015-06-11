start_index <- 1

d <- c(2,3,5,7,13,15,18,24,25,30,36,42,50,64,87,95,108,122)
d <- d[start_index:length(d)]
patients_log <- log(d)

x <- 1:length(patients_log)

df <- data.frame(cbind(patients_log, x))
names(df) <- c("y","x")
fit <- lm("y ~ x", df)

jpeg("./mers_patients.jpg")
plot(patients_log)
abline(fit)
title(paste0("slope = ", toString(round(fit$coefficients[2],2))))
dev.off()