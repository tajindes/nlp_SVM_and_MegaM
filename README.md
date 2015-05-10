Name: Tajinder Singh

For SVM:
preprocessing:
1. Use svmpreprocessing.py to convert TRAINING DATA to TRAINING_FILE (spam.svm.training)
2. Then execute svm_learn to create spam.svm.nb (MODEL FILE);
3. Use svm_preprocessing_dev.py to convert TEST DATA to TEST_FIEL (spam.svm.test)
4. Then execute the svm_classify to crete spam.svm.output file.
5. Post process the output using file svmpostprocess_spam.py to convert ouput file to spam.svm.out
Note: use svmpostprocess_sentiment.py in case of sentiment analysis to get sentiment.svm.out file.

For MegaM
1. Use megampreprocess.py for preprocessing.
2. Usemegampostprocess_spam.py for post processing of spam output file (spam.megam.output) to get spam.megam.out file
3. Use megampostprocess_sentiment.py for post processing of sentiment output file (sentiment.megam.output) to get sentiment.megam.out file.


# Precision, Recall and F-score on the development data for Naive Bayes Classifier for each of the two datasets:

SVM SPAM:
item is: HAM
precision for class HAM  is: 0.7634598411297441
recall for class HAM  is: 0.865
F-SCORE for class HAM  is: 0.8110642287857478
item is: SPAM
precision for class SPAM  is: 0.41304347826086957
recall for class SPAM  is: 0.26170798898071623
F-SCORE for class SPAM  is: 0.3204047217537943

SVM SENTIMENT:
item is: NEG
precision for class NEG  is: 0.5536244171259008
recall for class NEG  is: 0.2612
F-SCORE for class NEG  is: 0.3549395298274222
item is: POS
precision for class POS  is: 0.5165554246826332
recall for class POS  is: 0.7894
F-SCORE for class POS  is: 0.6244759117158454

MEGAM:
class: HAM
precision for class HAM  is: 0.9266917293233082
recall for class HAM  is: 0.986
F-SCORE for class HAM  is: 0.9554263565891473
class: SPAM
precision for class SPAM  is: 0.9531772575250836
recall for class SPAM  is: 0.7851239669421488
F-SCORE for class SPAM  is: 0.8610271903323263

SENTIMENT:
class: NEG
precision for class NEG  is: 0.7392809587217044
recall for class NEG  is: 0.7402666666666666
F-SCORE for class NEG  is: 0.7397734843437708
class: POS
precision for class POS  is: 0.7399198931909212
recall for class POS  is: 0.7389333333333333
F-SCORE for class POS  is: 0.7394262841894598
