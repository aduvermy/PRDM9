##5000X
pond_1surx=read.table('projetMaster/testponderation/essai_1surx')
pond_1surx_rang=read.table('projetMaster/testponderation/essai_diffrang_1surx.txt')
pond_1surexp100moins20x_rang=read.table('projetMaster/testponderation/essai_diffrang_exp100-20x.txt')
pond_1surexp100moins15x_rang=read.table('projetMaster/testponderation/essai_exp100-15x.txt')
pond_1surexp100moins20x=read.table('projetMaster/testponderation/essai_exp100-20x')
pond_1surexp100moins30x=read.table('projetMaster/testponderation/essai_exp100-30x')
pond_1surexp150moins30x=read.table('projetMaster/testponderation/essai_exp150-30x.txt')
pond_1surexp5moins0.5x=read.table('projetMaster/testponderation/essai_exp5-0.5x')
pond_1surexp5moins0.8x=read.table('projetMaster/testponderation/essai_exp5-0.8x')
pond_rang=read.table('projetMaster/testponderation/essai_rang.txt')
pond_0=read.table('projetMaster/testponderation/essai_sansponderationsansrang')
data5000X=c(pond_0=length(pond_0$V1),pond_rang=length(pond_rang$V1),pond_1surexp5moins0.8x=length(pond_1surexp5moins0.8x$V1),
            pond_1surexp5moins0.5x=length(pond_1surexp5moins0.5x$V1),pond_1surexp150moins30x=length(pond_1surexp150moins30x$V1),
            pond_1surexp100moins15x_rang=length(pond_1surexp100moins15x_rang$V1),
            pond_1surx_rang=length(pond_1surx_rang$V1),pond_1surx=length(pond_1surx$V1),
            pond_1surexp100moins30x=length(pond_1surexp100moins30x$V1))

###20X
##resultats faux
pond_1surx_20=read.table('projetMaster/20x/essai_1surx.txt')
pond_1surx_rang_20=read.table('projetMaster/20x/essai_1surxrang.txt')
pond_1surexp100moins20x_rang_20=read.table('projetMaster/20x/essai_ex100-20rang.txt')
pond_1surexp100moins15x_rang_20=read.table('projetMaster/20x/essai_ex100-15rang.txt')
#pond_1surexp100moins20x_20=read.table('projetMaster/20x/essai_ex100-20.txt')
pond_1surexp100moins30x_20=read.table('projetMaster/20x/essai_ex100-30.txt')
pond_1surexp150moins30x_20=read.table('projetMaster/20x/essai_ex150-30.txt')
pond_1surexp5moins0.5x_20=read.table('projetMaster/20x/essai_ex5-5.txt')
pond_1surexp5moins0.8x_20=read.table('projetMaster/20x/essai_ex5-8.txt')
pond_rang_20=read.table('projetMaster/20x/essai_rang.txt')
pond_0_20=read.table('projetMaster/20x/essai_0pond.txt')
data20X=c(pond_0=length(pond_0_20$V1),pond_rang=length(pond_rang_20$V1),pond_1surexp5moins0.8x=length(pond_1surexp5moins0.8x_20$V1),
            pond_1surexp5moins0.5x=length(pond_1surexp5moins0.5x_20$V1),pond_1surexp150moins30x=length(pond_1surexp150moins30x_20$V1),
            pond_1surexp100moins15x_rang=length(pond_1surexp100moins15x_rang_20$V1),
            pond_1surx_rang=length(pond_1surx_rang_20$V1),pond_1surx=length(pond_1surx_20$V1),
            pond_1surexp100moins30x=length(pond_1surexp100moins30x_20$V1))

###courbe de ponderation visualisation
data=data.frame(row.names=(c('zeroPonderation','rangPonderation','1/1+exp(5-0.8x)','1/1+exp(5-0.5x)','1/1+exp(150-30x)','1/1+exp(100-15x) et rang','1/x et rang','1/x','1/1+exp(100-30x)')),"5000X"=data5000X/2,"20X"=data20X/2)
data <- data[order(data$X5000X),]
par(mfrow=c(1,2))
dotchart(data$X5000X, labels = row.names(data), cex = 0.6, xlab = "nombres erreurs", main='Essais pondération')

curve(expr=1/(1 + exp(150-30*x)), from=0, to=30, col='Red', xlab='x', ylab='y', main='courbe de pondération',ylim=c(0,2))
curve(expr=1/(1 + exp(100-30*x)), from=0, to=30, col='brown', add=TRUE)
#curve(expr=1/(1 + exp(100-20*x)), from=0, to=30, col='black', add=TRUE,lty=2)
curve(expr=1/(1 + exp(100-15*x)), from=0, to=30, col='pink', add=TRUE)
curve(expr=1/(1 + exp(5-0.8*x)), from=0, to=30, col='blue', add=TRUE)
curve(expr=1/(1 + exp(5-0.5*x)), from=0, to=30, col='black', add=TRUE)
curve(expr=1/x, from=0, to=30, col='chartreuse', add=TRUE)
legend("bottomright", legend=c("a", "b","c","c","d","e"),col=c("red", "brown","black","pink","blue","chartreuse"),lty=1,cex=0.75,ncol=2)


##resultats à differente couv
err_1000X=read.table('/home/arnaud/projetMaster/vdsheb/essai_diffrang_1000x_grep.txt')
err_1000X2=read.table('/home/arnaud/projetMaster/vdsheb/essai_diffrang_1000x_2.txt')
err_1000X3=read.table('/home/arnaud/projetMaster/vdsheb/essai1000vs5000.txt')
err_100X=read.table('/home/arnaud/projetMaster/vdsheb/essai_diffrang_100x_1.txt')
err_100X2=read.table('/home/arnaud/projetMaster/vdsheb/essai_diffrang_100x_2.txt')
err_100X3=read.table('/home/arnaud/projetMaster/vdsheb/essai_diffrang_100x_grep.txt')
err_10X=read.table('/home/arnaud/projetMaster/vdsheb/essai_diffrang_10x_grep.txt')
err_10X2=read.table('/home/arnaud/projetMaster/vdsheb/essai_diffrang_10x_2.txt')
err_10X3=read.table('/home/arnaud/projetMaster/vdsheb/essai10vs5000.txt')
err_50X=read.table('/home/arnaud/projetMaster/vdsheb/essai_diffrang_50x_grep.txt')
err_50X2=read.table('/home/arnaud/projetMaster/vdsheb/essai_diffrang_50x_2.txt')
err_50X3=read.table('/home/arnaud/projetMaster/vdsheb/essai50vs5000.txt')

err_5X=read.table('/home/arnaud/projetMaster/vdsheb/essai_diffrang_5x_grep.txt')
err_5X2=read.table('/home/arnaud/projetMaster/vdsheb/essai_diffrang_5x_grep.txt')
err_5X3=read.table('/home/arnaud/projetMaster/vdsheb/essai5vs5000.txt')
dtaerror=data.frame('couverture'=c('5X','10X','50X','100X','1000X','5000X'),'nombre erreurs'=c(length(err_5X$V1)/2,length(err_10X$V1)/2,length(err_50X$V1)/2,length(err_100X$V1)/2,length(err_1000X$V1)/2,length(err_5000X$V1)/2))
dtaerror<-dtaerror[order(dtaerror$nombre.erreurs),]
essai1<-c(length(err_5X$V1)/2,length(err_10X$V1)/2,length(err_50X$V1)/2,length(err_100X$V1)/2,length(err_1000X$V1)/2,length(err_5000X$V1)/2)
essai2<-c(length(err_5X2$V1)/2,length(err_10X2$V1)/2,length(err_50X2$V1)/2,length(err_100X2$V1)/2,length(err_1000X2$V1)/2,length(err_5000X$V1)/2)
essai3<-c(length(err_5X3$V1)/2,length(err_10X3$V1)/2,length(err_50X3$V1)/2,length(err_100X3$V1)/2,length(err_1000X3$V1)/2,length(err_5000X$V1)/2)
dta<-data.frame('5X'=c(length(err_5X$V1)/2,length(err_5X2$V1)/2,length(err_5X3$V1)/2),'10X'=c(length(err_10X$V1)/2,length(err_10X2$V1)/2,length(err_10X3$V1)/2),'50X'=c(length(err_50X$V1)/2,length(err_50X2$V1)/2,length(err_50X3$V1)/2),'100X'=c(length(err_100X$V1)/2,length(err_100X2$V1)/2,length(err_100X3$V1)/2),'1000X'=c(length(err_1000X$V1)/2,length(err_1000X2$V1)/2,length(err_1000X3$V1)/2),'5000X'=c(length(err_5000X$V1)/2,length(err_5000X$V1)/2,length(err_5000X$V1)/2))
dta<-rbind(dta,essai1,essai2,essai2,essai3)
dta2<-data.frame(row.names=(c('5X','10X','50X','100X','1000X','5000X')),'essai1'=essai1/406*100, 'essai2'=essai2/406*100,'essai3'=essai3/406*100)
boxplot(t(dta2))
boxplot(t(dta2),main="Pourcentage d'erreurs de PRDM9scan en fonction de la couverture", xlab='couverture',ylab="pourcentage d'erreurs")