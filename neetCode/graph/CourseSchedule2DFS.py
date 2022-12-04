class CourseSchedule2DFS:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # our first task is to build an adjacency list with the prerequisites
        # initially for every course we are going to map it to an empty list
        coursePrerequisites={course:[] for course in range(numCourses) }
        # for every single course and its prerequisite pair given in the question, create an adjacency list
        for courseWithPrereq , prereqOfCourse in prerequisites:
            coursePrerequisites[courseWithPrereq].append(prereqOfCourse)

        # a course can have 3 possible states : visited(Course has already been added to the output), visiting (Course hasn't been added to the output but added to the cycle) and unvisited (Course hasn't been added to the output or the cycle yet.)

        # output list to return the order in which course should be taken considering the prerequisites of individual course.
        output=[]
        visited, hasCycle=set(), set() #defined outside function to keep the courseNumber for different stages of recursion.

        #depthFirstSerch method is created inside the function so that the new declaration of the above variables isn't needed and would be already accessible within this function.
        def depthFirstSerch(courseNumber):
            if courseNumber in hasCycle:
                #  if course number is encountered again, that means there is a cycle.
                return False

            if courseNumber in visited:
                # if course is found in visited set, In recursion, it should return true as its checking whether the course has already been visited or not.
                return True

            # now if the above two conditions are skipped we will add it to our cycle set so that we can figure out whether there is a cycle or not , if the parameter of this method has the course that is in the cycle set.
            hasCycle.add(courseNumber)

            for everyPrerequisiteOfThisParticularCourseNumber in coursePrerequisites[courseNumber]:
                #  run depthFirstSearch on the each and every courseNumber that is the prerequisite to the current course(method argument).
                if depthFirstSerch(everyPrerequisiteOfThisParticularCourseNumber)==False:
                    #   this means we have found a loop hence return false
                    return False
                #if it doesn't equals false, then we are going to continue to go through all the prerequisites and continue to run depth first search.

            # When all of that is done, it means the courses that we are considering in hasCycle set will not surely form a cycle as we have verified and passed that set of courses, hence we will remove it from the hasCycle set
            hasCycle.remove(courseNumber)
            #Also we can add this particular courseNumber to visit as we just went through all the prerequisites of this course.
            visited.add(courseNumber)
            #As this course is visited and its prerequisites have been depthFirstSearched, we can add this course to our final output list
            output.append(courseNumber)
            #As we have got true in the prerequisites of this course we can return true
            return True

        # Go through every course in given number of courses
        for everyCourse in range(numCourses): #here if the total number of course are 4 then the course ID's will be: 0,1,2 and 3
            #when Depth First Search would detect a cycle, the method will return false,  hence the prerequisites course order is erroneous, so we will return an empty list
            if depthFirstSerch(everyCourse) ==False:
                return []
        #if everything goes well and the above for loop completes executing, it means there was no error (cycle) in the course schedule and we have retrived the schedule order in output list.
        return output
