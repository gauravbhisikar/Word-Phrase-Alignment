stanford_parser_path='/home/aditya/stanford-parser-4.2.0/stanford-parser-full-2020-11-17'

java -mx1000m -cp $stanford_parser_path/*:  edu.stanford.nlp.parser.lexparser.LexicalizedParser -retainTMPSubcategories -outputFormat "oneline"  edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz $* 1> $1-parsed-output 2>$1-parse.log

python parser-modification.py $1-parsed-output > modified-output
cat header  modified-output list-processing.py > list-processing1.py
python list-processing1.py
