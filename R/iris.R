#====决策树====
da <- iris
index <- c(sample(1:50,40),
           sample(51:100,40),
           sample(101:150,40))
Tr <- da[index,]
Te <- da[-index,]
library(rpart)
modle <- rpart(Species~.,data = Tr)
res <- predict(modle,Te[,-5],type = 'class')
table(Te[,5],res)


#====人工神经网络====
library(nnet)
da <- iris
index <- c(sample(1:50,40),
           sample(51:100,40),
           sample(101:150,40))
Tr <- da[index,]  #训练集
Te <- da[-index,] #测试集
out <- class.ind(da$Species)
Net <- nnet(Tr[1:4],out[index,],size = 10,softmax = T)
res<- predict(Net,Te[1:4],type='class')
table(Te[,5],res)
