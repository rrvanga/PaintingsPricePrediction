n<-`Final_Input`
n$imagelink.href<-NULL
n$title<-NULL
n$artist<-NULL
n$price<-NULL
n$size<-NULL
str(n)
n$�..imagelink<-NULL
library(nnet)
n$price.bracket<-as.factor(n$price.bracket)
n$orientation<-as.numeric(factor(n$orientation,levels=c("landscape","square","portrait")))-1
n$size.category<-as.numeric(factor(n$size.category,levels=c("L","M","S")))-1
Traindata<-n[1:700,]
Testdata<-n[701:1048,]
model<-multinom(price.bracket~height+width+views+favorites+orientation+size.category+mediums+subject+date+country,data=Traindata)
Testdata$pred<-predict(model,Testdata,type="class")
confusionMatrix<-table(Testdata$price.bracket,Testdata$pred)
confusionMatrix
MisclassificationRate<-1-sum(diag(confusionMatrix))/sum(confusionMatrix)
MisclassificationRate
Accuracy<-sum(diag(confusionMatrix))/sum(confusionMatrix)
Accuracy

