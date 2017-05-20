setwd('E://coding//R') 
n_row <- length(unique(tr_d[,1]))
n_col <- length(unique(tr_d[,2]))
te <- matrix(0,nrow = n_row,ncol = n_col)
rownames(te) <- unique(tr_d[,1])
colnames(te) <- unique(tr_d[,2])
#====用户浏览矩阵======
for(i in 1:nrow(tr_d)){
  te[as.character(tr_d[i,1]),tr_d[i,2]] <- 1
}
#====相关系数矩阵=====
cor <- matrix(0,nrow = n_col,ncol = n_col)
for(i in 1:n_col){
  for(j in 1:n_col){
    a <- sum(rowSums(te[,c(i,j)])==2)
    b <- sum(rowSums(te[,c(i,j)])!=0)
    cor[i,j] <- a/b
  }
}

cor <- read.table('cor.txt',header = F,sep = ',')
#====对行列重命名====
rownames(cor) <- unique(tr_d[,2])
colnames(cor) <- unique(tr_d[,2])
#===========IBCF==============================
#==构建列表：每个IP的浏览记录为一个子表===
te_l <- list()
vec <- unique(te_d[,1])
for(i in vec){
  ind <- te_d[,1] == i
  te_l[[as.character(i)]] <- te_d[ind,2]
}
#===推荐过程，根据用户的第一条浏览记录进行推荐===
input <- te_d   #===测试集===
ma <- matrix(0,nrow = nrow(input),ncol = 2)
rem <- cbind(input,ma)
for(i in 1:nrow(input)){
  if(input[i,2] %in% colnames(cor)){
    re <- which.max(cor[input[i,2],])
    re <- names(re)
    rem[i,3] <- re
    rem[i,4] <- re %in% te_l[[as.character(input[i,1])]]
  }
}
#====计算推荐准确率===
sum(rem[,3]==0)
p <- sum(rem[,4])/(nrow(rem)-sum(rem[,3]==0))
rem[1:20,4]
