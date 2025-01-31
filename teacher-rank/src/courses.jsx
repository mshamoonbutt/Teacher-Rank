function Course(){
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
    const courses = [
        {id: "comp1", name: "Complier Construction"},
        {id: "comp2", name: "Computer Network"},
        {id: "comp3", name: "Compter Organization"},
        {id: "comp4", name: "D&A of Algorithms"},
        {id: "comp5", name: "Data Structure of Algorithms"},
        {id: "comp6", name: "DataBase System"},
        {id: "comp7", name: "Digital Logic Design"},
    ];
    const courseItem = courses.map(course => <li key={course.id}><a href="#" style={linkStyle}>{course.name}</a></li>);
    return(
        <body style={styles}>
            <div>
                <h3 style={heading}>Choose the Course</h3>
            </div>
            <div>
                <ul style={listStyle}>
                    {courseItem}
                </ul>
            </div>
        </body>
    );
};
export default Course