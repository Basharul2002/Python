from typing import List, Dict, Set


# Define a structure to hold course information
class Course:
    def __init__(self, name: str, prerequisites: Set[int], course_credit: int):
        self.name = name
        self.prerequisites = prerequisites
        self.course_credit = course_credit


# Function to print available courses
def print_courses(courses: List[Course]):
    print("Available Courses:")
    for i, course in enumerate(courses):
        print(f"{i + 1}. {course.name}")


# Function to recommend next semester courses
def recommend_courses(all_courses: List[Course], completed_courses: List[int], total_credit_completed: int):
    completed_set = set(completed_courses)

    print("Recommended Courses:")
    for i, course in enumerate(all_courses):
        if i + 1 in completed_set:
            continue

        can_take = all(prereq in completed_set for prereq in course.prerequisites)

        if course.name == "RESEARCH METHODOLOGY" and total_credit_completed < 100:
            can_take = False

        if can_take:
            print(f"- {course.name}")


# Course Details for CSE
def CSECourse():
    all_courses = [
        # semester 1
        Course("DIFFERENTIAL CALCULUS & CO-ORDINATE GEOMETRY", set(), 3),
        Course("PHYSICS 1", set(), 3),
        Course("PHYSICS 1 LAB", {1}, 1),
        Course("ENGLISH READING SKILLS & PUBLIC SPEAKING", set(), 3),
        Course("INTRODUCTION TO PROGRAMMING", set(), 3),
        Course("INTRODUCTION TO PROGRAMMING LAB", {5}, 1),
        Course("INTRODUCTION TO COMPUTER STUDIES", set(), 1),

        # semester 2
        Course("DISCRETE MATHEMATICS", {1, 5}, 3),
        Course("INTEGRAL CALCULUS & ORDINARY DIFFERENTIAL EQUATIONS", {1}, 3),
        Course("OBJECT ORIENTED PROGRAMMING 1", {5, 6}, 3),
        Course("PHYSICS 2", {2}, 3),
        Course("PHYSICS 2 LAB", {3}, 1),
        Course("ENGLISH WRITING SKILLS & COMMUNICATION", {4}, 3),
        Course("INTRODUCTION TO ELECTRICAL CIRCUITS", {2}, 3),
        Course("INTRODUCTION TO ELECTRICAL CIRCUITS LAB", {3}, 1),
        
        # semester 3
        Course("CHEMISTRY", {11}, 3),
        Course("COMPLEX VARIABLE,LAPLACE & Z-TRANSFORMATION", {9}, 3),
        Course("INTRODUCTION TO DATABASE", {10}, 3),
        Course("ELECTRONIC DEVICES", {14}, 3),
        Course("ELECTRONIC DEVICES LAB", {15}, 1),
        Course("PRINCIPLES OF ACCOUNTING", {9}, 3),
        Course("DATA STRUCTURE", {8, 10}, 3),
        Course("DATA STRUCTURE LAB", {8, 10}, 1),
        Course("COMPUTER AIDED DESIGN & DRAFTING", {}, 1),
        Course("ALGORITHMS", {22, 23}, 3),
        Course("MATRICES, VECTORS, FOURIER ANALYSIS", {17}, 3),
        Course("OBJECT ORIENTED PROGRAMMING 2", {10, 19}, 3),
        Course("OBJECT ORIENTED ANALYSIS AND DESIGN", {20}, 3),
        Course("BANGLADESH STUDIES", {6}, 3),
        Course("DIGITAL LOGIC AND CIRCUITS", {15}, 3),
        Course("DIGITAL LOGIC AND CIRCUITS LAB", {16}, 1),
        Course("COMPUTATIONAL STATISTICS AND PROBABILITY", {17}, 3),
        Course("THEORY OF COMPUTATION", {25}, 3),
        Course("PRINCIPLES OF ECONOMICS", {31}, 2),
        Course("BUSINESS COMMUNICATION", {28}, 3),
        Course("NUMERICAL METHODS FOR SCIENCE AND ENGINEERING", {25}, 3),
        Course("DATA COMMUNICATION", {31, 32}, 3),
        Course("MICROPROCESSOR AND EMBEDDED SYSTEM", {31, 32}, 3),
        Course("SOFTWARE ENGINEERING", {27, 28}, 3),
        Course("ARTIFICIAL INTELLIGENCE AND EXPERT SYS.", {25, 31}, 3),
        Course("COMPUTER NETWORKS", {37}, 3),
        Course("COMPUTER ORGANIZATION AND ARCHITECTURE", {38}, 3),
        Course("OPERATING SYSTEM", {25, 38}, 3),
        Course("WEB TECHNOLOGIES", {39}, 3),
        Course("ENGINEERING ETHICS", {38, 39}, 2),
        Course("COMPILER DESIGN", {32}, 3),
        Course("COMPUTER GRAPHICS", {25, 26}, 3),
        Course("ENGINEERING MANAGEMENT", {44}, 3),
        Course("RESEARCH METHODOLOGY", {}, 3),
        Course("ADVANCE DATABASE MANAGEMENT SYSTEM", {18}, 3),
        Course("BASIC MECHANICAL ENGG.", {11}, 3),
        Course("COMPUTER SCIENCE MATHEMATICS", {25, 36}, 3),
        Course("MANAGEMENT INFORMATION SYSTEM", {39}, 3),
        Course("SIGNALS & LINEAR SYSTEM", {26}, 3),
        Course("BASIC GRAPH THEORY", {25}, 3),
        Course("DIGITAL SYSTEM DESIGN", {42}, 3),
        Course("IMAGE PROCESSING", {47}, 3),
        Course("MULTIMEDIA SYSTEMS", {44}, 3),
        Course("SIMULATION & MODELING", {40}, 3),
        Course("ENTERPRISE RESOURCE PLANNING", {39, 54}, 3),
        Course("DATA WAREHOUSE AND DATA MINING", {83}, 3),
        Course("NATURAL LANGUAGE PROCESSING", {40, 77}, 3),
        Course("SOFTWARE DEVELOPMENT PROJECT MANAGEMENT", {67}, 3),
        Course("HUMAN COMPUTER INTERACTION", {40, 44}, 3),
        Course("ADVANCED COMPUTER NETWORKS", {41}, 3),
        Course("SOFTWARE REQUIREMENT ENGINEERING", {39}, 3),
        Course("COMPUTER VISION AND PATTERN RECOGNITION", {40, 47}, 3),
        Course("LINEAR PROGRAMMING", {40, 32}, 3),
        Course("NETWORK SECURITY", {41}, 3),
        Course("SOFTWARE QUALITY AND TESTING", {67}, 3),
        Course("ADVANCED OPERATING SYSTEM", {43}, 3),
        Course("DIGITAL DESIGN WITH SYSTEM [VERILOG,VHDL & FPGAS]", {97}, 3),
        Course("ROBOTICS ENGINEERING", {40}, 3),
        Course("BUSINESS INTELLIGENCE AND DECISION SUPPORT", {61}, 3),
        Course("TELECOMMUNICATIONS ENGINEERING", {37}, 3),
        Course("PROGRAMMING IN PYTHON", {44}, 3),
        Course("ADVANCED PROGRAMMING WITH JAVA", {44}, 3),
        Course("ADVANCED PROGRAMMING WITH .NET", {44}, 3),
        Course("ADVANCED PROGRAMMING IN WEB TECHNOLOGY", {44}, 3),
        Course("ADVANCED ALGORITHM TECHNIQUES", {40}, 3),
        Course("NETWORK RESOURCE MANAGEMENT & ORGANIZATION", {37, 41}, 3),
        Course("INTRODUCTION TO DATA SCIENCE", {40}, 3),
        Course("CYBER LAWS & INFORMATION SECURITY", {44}, 3),
        Course("BIOINFORMATICS", {40}, 3),
        Course("PARALLEL COMPUTING", {25, 40}, 3),
        Course("MACHINE LEARNING", {40}, 3),
        Course("WIRELESS SENSOR NETWORKS", {37, 41}, 3),
        Course("INDUSTRIAL ELECTRONICS, DRIVES & INSTRUMENTATION", {30}, 3),
        Course("MOBILE APPLICATION DEVELOPMENT", {44}, 3),
        Course("SOFTWARE ARCHITECTURE AND DESIGN PATTERNS", {67}, 3),
        Course("DIGITAL MARKETING", {44, 54}, 3),
        Course("E-COMMERCE, E-GOVERNANCE & E-SERIES", {44}, 3),
        Course("DIGITAL SIGNAL PROCESSING", {55}, 3),
        Course("VLSI CIRCUIT DESIGN", {91}, 3),
    ]

    # Print available courses
    print_courses(all_courses)

    print("\n\n")
    # Get completed courses from the user
    line = input("Enter completed course numbers separated by spaces: ")
    completed_courses = list(map(int, line.split()))

    # Calculate total credit for completed courses
    total_credit_completed = 0
    for course_num in completed_courses:
        if 1 <= course_num <= len(all_courses):
            index = course_num - 1
            total_credit_completed += all_courses[index].course_credit

    print(f"Total credit completed: {total_credit_completed}")

    # Recommend next semester courses
    recommend_courses(all_courses, completed_courses, total_credit_completed)

def EEECourse():
    all_courses = [
        Course("DIFFERENTIAL CALCULUS & CO-ORDINATE GEOMETRY", set(), 3),
        Course("PHYSICS 1", set(), 3),
        Course("PHYSICS 1 LAB", {1}, 1),
        Course("ENGLISH READING SKILLS & PUBLIC SPEAKING", set(), 3),
    ]
if __name__ == "__main__":
    dept = input("Deparment Number \n1. CSE \n2. EEE \nChoose your departement: ")

    if (dept == "1"):
        CSECourse()
    
    elif (dept == "2"):
        EEECourse()
        
    else:
        print("Invalid Input")
