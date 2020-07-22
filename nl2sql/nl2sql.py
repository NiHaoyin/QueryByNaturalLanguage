import jieba
from db import Dictionary
import re


# 分词
def cut_words(input_words):
    jieba.load_userdict("db/Database Dic.txt")
    segments = list(jieba.cut(input_words))
    print("分词结果：", segments)
    return segments


def get_keys(d, value):
    return [k for k, v in d.items() if v == value]


# 自然语言转化为SQL
def nl2sql(segments, res):
    db_dic = Dictionary.create_dictionary()
    attr = list()
    value = list()
    what = list()
    table = list()
    for seg in segments:  # 扫描输入的自然语言
        if Dictionary.whether_in_dic(db_dic, seg):  # 判断扫描到的词在不在数据库同义词词典里
            seg = Dictionary.modify(db_dic, seg)
            table.append(Dictionary.choose_table(db_dic, seg))
            what.append(seg)
            continue
        else:  # 如果不在数据库词典里
            for element in res:
                a = get_keys(element, seg)  # 找到这个词语所对应的属性
                if a:
                    attr.append(re.sub('[学生.]', '', a[0]))
                    value.append(seg)
                    break
    # SQL中的select部分
    sql_what = 'select'
    j = len(what)-1
    while j >= 0:
        sql_what = sql_what + ' ' + str(what[j])
        j = j-1
        if j >= 0:
            sql_what = sql_what + ','
    # SQL中的from部分
    table = list(set(table))
    j = len(table)-1
    sql_from = 'from'
    while j >= 0:
        sql_from = sql_from + ' ' + str(table[j])
        j = j-1
    # SQL中的where部分
    i = len(attr)-1
    sql_where = 'where'
    while i >= 0:
        sql_where = sql_where+' '+str(attr[i])+'='+'\''+str(value[i])+'\''
        i = i-1
        if i >= 0:
            sql_where = sql_where+' and'
    sql = sql_what+' '+sql_from+' '+sql_where
    print("SQL：", sql)
    return sql






