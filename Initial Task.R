#Question1
#create dataset
sample1 <- data.frame(x1 = c(7, 8, 5, 7),
                      x2 = c(9, 10, 7, 11),
                      x3 = c(6, 7, 8, 7))
#variane-covariance matrix
matrix <- cov(sample1)
#compute pca
pca <- prcomp(sample1, scale. = TRUE)
pca
names(pca)
#loadings for the first principal component
loadings_PC1 <- pca$rotation[,1]
loadings_PC1
#Calculate the proportion of variance explained by the first two PCs
PVE <- sum(pca$sdev[1:2]^2)/sum(pca$sdev^2)
PVE