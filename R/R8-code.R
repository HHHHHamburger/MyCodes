setwd('E://coding//R')
Data <- read.table('Apriori-data.txt',sep = ',',header = T)
Data <- Data[,c(1:6,8)]
#====
A1 <- which(Data[,1] >= 0 & Data[,1] <= 0.179)
A2 <- which(Data[,1] > 0.350 & Data[,1] <= 0.504)
A3 <- which(Data[,1] > 0.179 & Data[,1] <= 0.258)
A4 <- which(Data[,1] > 0.258 & Data[,1] <= 0.35)
Data[A1,1] <- 'A1'
Data[A2,1] <- 'A2'
Data[A3,1] <- 'A3'
Data[A4,1] <- 'A4'
#====
B1 <- which(Data[,2] >= 0 & Data[,2] <= 0.15)
B2 <- which(Data[,2] > 0.296 & Data[,2] <= 0.485)
B3 <- which(Data[,2] > 0.485 & Data[,2] <= 0.78)
B4 <- which(Data[,2] > 0.15 & Data[,2] <= 0.296)
Data[B1,2] <- 'B1'
Data[B2,2] <- 'B2'
Data[B3,2] <- 'B3'
Data[B4,2] <- 'B4'
#====
C1 <- which(Data[,3] >= 0.438 & Data[,3] <= 0.61)
C2 <- which(Data[,3] > 0.288 & Data[,3] <= 0.415)
C3 <- which(Data[,3] >= 0.067 & Data[,3] <= 0.201)
C4 <- which(Data[,3] > 0.201 & Data[,3] <= 0.288)
Data[C1,3] <- 'C1'
Data[C2,3] <- 'C2'
Data[C3,3] <- 'C3'
Data[C4,3] <- 'C4'
#====
D1 <- which(Data[,4] > 0.176 & Data[,4] <= 0.256)
D2 <- which(Data[,4] > 0.364 & Data[,4] <= 0.552)
D3 <- which(Data[,4] > 0.256 & Data[,4] <= 0.364)
D4 <- which(Data[,4] >= 0.059 & Data[,4] <= 0.176)
Data[D1,4] <- 'D1'
Data[D2,4] <- 'D2'
Data[D3,4] <- 'D3'
Data[D4,4] <- 'D4'
#====
E1 <- which(Data[,5] > 0.375 & Data[,5] <= 0.526)
E2 <- which(Data[,5] > 0.154 & Data[,5] <= 0.256)
E3 <- which(Data[,5] > 0.256 & Data[,5] <= 0.375)
E4 <- which(Data[,5] >= 0.003 & Data[,5] <= 0.154)
Data[E1,5] <- 'E1'
Data[E2,5] <- 'E2'
Data[E3,5] <- 'E3'
Data[E4,5] <- 'E4'
#====
F1 <- which(Data[,6] >= 0.016 & Data[,6] <= 0.178)
F2 <- which(Data[,6] > 0.178 & Data[,6] <= 0.261)
F3 <- which(Data[,6] > 0.261 & Data[,6] <= 0.353)
F4 <- which(Data[,6] > 0.353 & Data[,6] <= 0.607)
Data[F1,6] <- 'F1'
Data[F2,6] <- 'F2'
Data[F3,6] <- 'F3'
Data[F4,6] <- 'F4'
Data[,7] <- as.character(Data[,7])





