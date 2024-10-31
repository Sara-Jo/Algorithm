/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
var findOrder = function (numCourses, prerequisites) {
  // Each key is a course, and its value is an array of courses that depend on it.
  const adjacencyList = new Map();

  // Array to keep track of the number of prerequisites (in-degree) for each course.
  const prerequesiteCounts = Array(numCourses).fill(0);

  // Queue to process courses with no remaining prerequisites.
  const processingQueue = [];

  for (const [course, prerequisite] of prerequisites) {
    if (adjacencyList.has(prerequisite)) {
      adjacencyList.get(prerequisite).push(course);
    } else {
      adjacencyList.set(prerequisite, [course]);
    }
    prerequesiteCounts[course]++;
  }

  // Initialize the processing queue with all courses that have no prerequisites.
  for (let course = 0; course < numCourses; course++) {
    if (prerequesiteCounts[course] === 0) {
      processingQueue.push(course);
    }
  }

  const courseOrder = [];

  while (processingQueue.length > 0) {
    // Dequeue the first course with no remaining prerequisites.
    const currentCourse = processingQueue.shift();

    // Add the course to the course order.
    courseOrder.push(currentCourse);

    // If the current course has courses that depend on it, process them.
    if (adjacencyList.has(currentCourse)) {
      for (const dependentCourse of adjacencyList.get(currentCourse)) {
        // Decrement the in-degree since one of its prerequisites has been "taken."
        prerequesiteCounts[dependentCourse]--;

        // If the dependent course now has no prerequisites, add it to the queue.
        if (prerequesiteCounts[dependentCourse] === 0) {
          processingQueue.push(dependentCourse);
        }
      }
    }
  }

  // If the courseOrder includes all courses, return it. Otherwise, return an empty array indicating it's impossible.
  return courseOrder.length === numCourses ? courseOrder : [];
};
