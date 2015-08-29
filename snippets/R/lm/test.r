# Function to fix coefficients
setCoeffs <- function(frml, weights, len){
  el <- paste0("offset(", weights[-1], "*", 
               unlist(strsplit(as.character(frml)[-(1:2)], " +\\+ +")), ")")
  el <- c(paste0("offset(rep(", weights[1], ",", len, "))"), el)                                 
  as.formula(paste(as.character(frml)[2], "~", 
                   paste(el, collapse = " + "), " + -1"))
}
# Example data
df <- data.frame(x1 = rnorm(10), x2 = rnorm(10, sd = 5), 
                 y = rnorm(10, mean = 3, sd = 10))
# Writing formula explicitly 
frml <- y ~ x1 + x2
# Basic model
mod <- lm(frml, data = df)
# Prime coefficients and any modifications. Note that "weights" contains 
# intercept value too
weights <- mod$coef
# Setting coefficient of x1. All the rest remain the same
weights[2] <- 3
# Final model
mod2 <- update(mod, setCoeffs(frml, weights, nrow(df)))
# It is fine that mod2 returns "No coefficients"
