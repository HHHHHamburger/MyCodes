setwd('E://coding//R') 

#apriori_data <- read_table('processedfile.txt',sep = ',', header = T)
apriori_data <- read_delim('processedfile.txt',delim = ',',col_types = c('l','l','l','l','l','l','l'))
apdata <- as(apriori_data,'transactions')
#apriori(apdata,parameter = list())
res <- apriori(apdata,parameter = list(support=0.06,confidence=0.75))
inspect(res)

#====k-means====
x <- 1:100
y <- 101:200
k <- 2
center1 <- c(x[1],y[1])
center2 <- c(x[2],y[2])
dis <- matrix(nrow = length(x),ncol = k+1)
while(T){
  for(i in 1:length(x)){
    dis[i,1] <- sqrt((x[i]-center1[1])^2+(y[i]-center1[2])^2)
    dis[i,2] <- sqrt((x[i]-center2[1])^2+(y[i]-center2[2])^2)
    dis[i,3] <- which.min(dis[i,1:2])
  }
  index1 <- dis[,3]==1
  index2 <- dis[,3]==2
  center1_new <- c(mean(x[index1]),mean(y[index1]))
  center2_new <- c(mean(x[index2]),mean(y[index2]))
  
  if((sum(center1==center1_new)+sum(center2==center2_new))==4){
    break
  }
  center1 <- center1_new
  center2 <- center2_new
}


#====人工神经网络====
library(nnet)
da <- read.table('processedfile.txt',sep = ',',header = T,stringsAsFactors = F)
da <- da[,c(1:6,8)]
index <- sample(1:nrow(da),0.8*nrow(da))
Tr <- da[index,]
Te <- da[-index,]
out <- class.ind(da[,7])
Net <- nnet(Tr[,-7],out[index,],size = 40,softmax = T,maxit=500)
res <- predict(Net,Te[,-7],type='class')
table(Te[,7],res)