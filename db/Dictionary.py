from anytree import Node, search, util

# 这是数据库同义词词典，总体呈树状结构。根节点为视图
# 往下为表格名称，同义词词义，具体词语
# 会这棵树中搜索扫描到的词语，将它替换成数据库使用的名称


def create_dictionary():
    root = Node("Students Database")
    student_course = Node("选课", parent=root)
    course_name = Node("course_name", parent=student_course)
    course_name_1 = Node("课程名", parent=course_name)
    course_name_2 = Node("课程名称", parent=course_name)
    course_name_3 = Node("课名", parent=course_name)
    course_name_4 = Node("课程", parent=course_name)
    course_name_5 = Node("名称", parent=course_name)
    course_number = Node("course_number", parent=student_course)
    course_number_1 = Node("课程号", parent=course_number)
    course_number_2 = Node("课程编号", parent=course_number)
    course_number_3 = Node("课程号码", parent=course_number)
    student_name = Node("student_name", parent=student_course)
    student_name_1 = Node("姓名", parent=student_name)
    student_name_2 = Node("名字", parent=student_name)
    student_name_3 = Node("学生名字", parent=student_name)
    student_name_3 = Node("学生", parent=student_name)
    student_name_4 = Node("学生姓名", parent=student_name)
    student_name_5 = Node("同学", parent=student_name)
    teacher_name = Node("teacher_name", parent=student_course)
    teacher_name_1 = Node("任课教师", parent=teacher_name)
    teacher_name_2 = Node("教师", parent=teacher_name)
    teacher_name_3 = Node("教授", parent=teacher_name)
    teacher_name_4 = Node("任课老师", parent=teacher_name)
    teacher_name_5 = Node("老师", parent=teacher_name)
    grade = Node("grade", parent=student_course)
    grade_1 = Node("成绩", parent=grade)
    grade_2 = Node("分数", parent=grade)
    grade_3 = Node("最终分数", parent=grade)
    grade_4 = Node("最终成绩", parent=grade)
    credit = Node("credit", parent=student_course)
    credit_1 = Node("学分", parent=credit)

    association = Node("交大社团", parent=root)
    association_name = Node("association_name", parent=association)
    association_name_1 = Node("社团名称", parent=association_name)
    association_name_2 = Node("社团", parent=association_name)
    association_type = Node("association_type", parent=association)
    association_type_1 = Node("社团类型", parent=association_type)
    association_type_2 = Node("类型", parent=association_type)
    association_location = Node("association_location", parent=association)
    association_location_1 = Node("活动地点", parent=association_location)
    association_location_2 = Node("活动教室", parent=association_location)
    association_location_3 = Node("地盘", parent=association_location)
    association_location_4 = Node("活动地盘", parent=association_location)
    association_leader = Node("association_leader", parent=association)
    association_leader_1 = Node("社长", parent=association_leader)
    association_leader_2 = Node("老大", parent=association_leader)
    association_number = Node("association_number", parent=association)
    association_number_1 = Node("人数", parent=association_number)
    association_number_2 = Node("成员数量", parent=association_number)
    association_number_3 = Node("多少人", parent=association_number)
    return root


def modify(root, word):
    a = search.find_by_attr(root, word)
    return a.parent.children[0].name


def whether_in_dic(root, word):
    flag = False
    if search.find_by_attr(root, word):
        flag = True
    return flag


def choose_table(root, word):
    node = search.find_by_attr(root, word)
    b = util.commonancestors(node)[1].name
    return b


