function Home(){
    const styles = {
        textAlign : "center",
        color: "pink",
        textDecoration: "none",
        fontSize: "18px"
    }
    const linkStyle = {
        color: "pink",
        textDecoration: "none",
        fontSize: "18px",
    }
    const listStyle = {
        listStyleType: "none", // This removes the bullet points
        paddingLeft: "0", // Optional: Removes default left padding
    }
    const courses = [
        {id: "comp", name: "COMP"},
        {id: "cscs", name: "CSCS"},
        {id: "arts", name: "Arts"},
        {id: "biol", name: "BIOL"},
        {id: "biot", name: "BIOT"},
        {id: "busn", name: "BUSN"},
        {id: "chem", name: "CHEM"},
        {id: "chin", name: "CHIN"},
        {id: "crim", name: "CRIM"},
        {id: "crst", name: "CRST"},
        {id: "econ", name: "ECON"},
        {id: "educ", name: "EDUC"},
        {id: "engl", name: "ENGL"},
        {id: "envr", name: "ENVR"},
        {id: "fren", name: "FREN"},
        {id: "geog", name: "GEOG"},
        {id: "grmn", name: "GRMN"},
        {id: "hist", name: "HIST"},
        {id: "hped", name: "HPED"},
        {id: "islm", name: "ISLM"},
        {id: "korn", name: "KONR"},
        {id: "ling", name: "LING"},
        {id: "math", name: "MATH"},
        {id: "mcom", name: "MCOM"},
        {id: "musc", name: "MUSC"},
        {id: "phil", name: "PHIL"},
        {id: "phys", name: "PHYS"},
        {id: "pkst", name: "PKST"},
        {id: "plsc", name: "PLSC"},
        {id: "psyc", name: "PSYC"},
        {id: "socl", name: "SOCL"},
        {id: "stat", name: "STAT"},
        {id: "univ", name: "UNIV"},
        {id: "urdu", name: "URDU"},
        {id: "wrcm", name: "WRCM"}
    ]
    const courseItem = courses.map(course => <li key={course.id}><a href="#" style={linkStyle}>{course.name}</a></li>)
    return(
        <body style={styles}>
            <div>
                <h1>Welcome to Teacher Rank</h1>
            </div>
            <div>
                <h3>Choose the department</h3>
            </div>
            <div>
                <ul style={listStyle}>
                    {courseItem}
                </ul>
            </div>
        </body>
    );
};
export default Home