function Rating(){
    const teachers = [
        {id: "1", name: "Aniqe Atiq", rating: 4.8, class_attendance: 3.0, grading: 3.0, class_environment: 3.0, quiz_assign: 2.1, leniency: 2.1}
    ];
    const teacherItem = teachers.map(teacher => <li key={teacher.id}><a href="#">{teacher.name}</a>: Rating:{teacher.rating}</li>);
    const teacherRating = teachers.map(teacher => <li key={teacher.id}>Attendance:{teacher.class_attendance}: Grading:{teacher.grading} Class Environment:{teacher.class_environment} Quiz/Assignments:{teacher.quiz_assign} Leniency:{teacher.leniency}</li>);
    return(
        <body>
            <div>
                <h3>Instructors</h3>
            </div>
            <div>
                <ul>
                    {teacherItem}
                    {teacherRating}
                </ul>
            </div>
        </body>
    );
};
export default Rating