function Course(){
    const courses = [
        {id: "comp1", name: "Complier Construction"},
        {id: "comp2", name: "Computer Network"},
        {id: "comp3", name: "Compter Organization"},
        {id: "comp4", name: "D&A of Algorithms"},
        {id: "comp5", name: "Data Structure of Algorithms"},
        {id: "comp6", name: "DataBase System"},
        {id: "comp7", name: "Digital Logic Design"},
    ];
    const courseItem = courses.map(course => <li key={course.id}><a href="#">{course.name}</a></li>);
    return(
        <body>
            <div>
                <h3>Choose the Course</h3>
            </div>
            <div>
                <ul>
                    {courseItem}
                </ul>
            </div>
        </body>
    );
};
export default Course