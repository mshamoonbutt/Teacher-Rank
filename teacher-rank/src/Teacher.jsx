function Teacher(){
    const teachers = [
        {id: "1", name: "Aniqe Atiq", rating: 4.8},
        {id: "2", name: "Samiya Qureshi", rating: 4.5},
        {id: "3", name: "Nazim Ashraf", rating: 2.1},
        {id: "4", name: "Fakhir Shaheen", rating: 4.1},
        {id: "5", name: "Amber Nisar", rating: 4.4},
    ];
    const teacherItem = teachers.map(teacher => <li key={teacher.id}><a href="#">{teacher.name}</a>: Rating:{teacher.rating}</li>);
    return(
        <body>
            <div>
                <h3>Instructors</h3>
            </div>
            <div>
                <ul>
                    {teacherItem}
                </ul>
            </div>
        </body>
    );
};
export default Teacher