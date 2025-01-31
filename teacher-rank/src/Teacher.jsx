function Teacher(){
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
        {id: "1", name: "Aniqe Atiq", rating: 4.8},
        {id: "2", name: "Samiya Qureshi", rating: 4.5},
        {id: "3", name: "Nazim Ashraf", rating: 2.1},
        {id: "4", name: "Fakhir Shaheen", rating: 4.1},
        {id: "5", name: "Amber Nisar", rating: 4.4},
    ];
    const teacherItem = teachers.map(teacher => <li key={teacher.id}><a href="#" style={linkStyle}>{teacher.name}</a>: Rating:{teacher.rating}</li>);
    return(
        <body style={styles}>
            <div>
                <h3 style={heading}>Instructors</h3>
            </div>
            <div>
                <ul style={listStyle}>
                    {teacherItem}
                </ul>
            </div>
        </body>
    );
};
export default Teacher