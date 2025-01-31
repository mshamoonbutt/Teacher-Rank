function Rating(){
    const styles = {
        textAlign : "center",
        color: "pink",
        textDecoration: "none",
        fontSize: "18px"
    }
    const linkStyle = {
        color : "pink",
        textDecoration: "none",
        fontSize: "18px",
    }
    const listStyle = {
        listStyleType: "none", // This removes the bullet points
        paddingLeft: "0", // Optional: Removes default left padding
    }
    const heading = {
       fontSize : "30px",
       textDecoration : "underLine"
    }
    const teachers = [
        {id: "1", name: "Aniqe Atiq", rating: 4.8, class_attendance: 3.0, grading: 3.0, class_environment: 3.0, quiz_assign: 2.1, leniency: 2.1}
    ];
    const teacherItem = teachers.map(teacher => <li key={teacher.id}><a href="#" style ={linkStyle}>{teacher.name}</a>: Rating:{teacher.rating}</li>);
    const teacherRating = teachers.map(teacher => <li key={teacher.id}>Attendance:{teacher.class_attendance} Grading:{teacher.grading} Class Environment:{teacher.class_environment} Quiz/Assignments:{teacher.quiz_assign} Leniency:{teacher.leniency}</li>);
    return(
        <body style={styles}>
            <div>
                <h3 style={heading}>Instructors</h3>
            </div>
            <div>
                <ul style={listStyle}>
                    {teacherItem}
                    {teacherRating}
                </ul>
            </div>
        </body>
    );
};
export default Rating