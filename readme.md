# Naive Bayes

A classifier program in python. Reads data given in data.csv file and predicts next outcome of inputs.  

* [Naive Bayes classifier](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)

# Usage & Example

```sh
$ # In this scenario, we have list of people with their skills, either hired or not.
$ # We let the program to predirect the next outcome.
$ python3 main.py data.csv "hire" "age:<30" "gpa:>3" "projects:>10" "certificates:>10" "languages:1" "soldiery:Tescilli"
P(no|<30,>3,>10,>10,1,Tescilli) = 6.858121104071436e-05
P(yes|<30,>3,>10,>10,1,Tescilli) = 0.00038277959993521216
The classified class is 'yes'
$ # The one with lower value means it has greater possibility. The classification as hiring result is a "yes".
```
