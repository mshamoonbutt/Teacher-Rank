function Header(){
    const styles = {
        backgroundColor: "purple",  // Set background color to purple
        textAlign: "center",
        padding: "15px",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        color: "pink",
        fontFamily: "Times New Roman, serif"
    };
    
    const navStyles = {
        display: "flex",
        listStyle: "none",
        gap: "15px",
        padding: 0
    };
    
    const linkStyles = {
        color: "pink",
        textDecoration: "none",
        fontSize: "18px"
    };
    return (
        <header style={styles}>
            <nav style={{ width: "100%", display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                <div>
                    <a href="#" style={linkStyles}><h1>Logo</h1></a>
                </div>
                <div>
                    <ul style={navStyles}>
                        <li><a href="#" style={linkStyles}>About us</a></li>
                        <li><a href="#" style={linkStyles}>back</a></li>
                    </ul>
                </div>
            </nav>
        </header>
    );
};
export default Header