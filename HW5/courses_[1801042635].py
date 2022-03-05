# *********************************************
# *  321 Programming Languages                *
# *  Fall 2021                                *
# *  Author: Yunus Emre Geyik                 *
# *  File  : courses_[1801042635].py          *
# *                                           *
# *  Finds the maximum number of courses.     * 
# *********************************************


# Finds the maximum number of courses problem solved via Greedy Algortihm
# After the student takes a course, it is checked whether the student can take another course as follows:
# The finish time of the previous course must be less than the start time of the new course to be taken. 
# When this rule is followed, the student can take the course.

def MaxNumberCourses( start_time , finish_time, courses):
    length = len(start_time)                     # length of the start array
    print ("Student can attend this courses : ")

    
    print (courses[0])     # The student always chooses the first course because the first course with the earliest start time
                        
    counter=0           # counter for the courses that student can attend
    index1 = 0                      # a index counter for the finish_time array
   
    for index2 in range(0,length):

        # If this course has start time greater than
        # or equal to the finish time of previously
        # selected course, then select it
        if (start_time[index2] >= finish_time[index1]):
            #The counter increments by 1 when the student takes a course.
            counter+=1
            # If the number of courses taken by the student is equal to 4, since he cannot take any more courses, 
            # the loop is exited and no more controls are made
            if(counter==4):
                break
            print (courses[index2])
            
            index1 = index2       # now new finish time index is the new course's start time index

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

# Driver code
if __name__ == "__main__":
    courses = ["English","Mathematics","Physics","Chemistry","Biology","Geography"]    # courses
    start_time = [1 , 3 , 0 , 5 , 8 , 5]                                               # courses's start time
    finish_time = [2 , 4 , 6 , 7 , 9 , 9]                                              # courses's finish time
        
    print ("The Courses :{} ".format(courses))
    print ("The Courses Start Times :{} ".format(start_time))
    print ("The Courses Finish Times :{} \n".format(finish_time))

    MaxNumberCourses(start_time , finish_time,courses)

