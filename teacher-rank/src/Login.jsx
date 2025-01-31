function Login(){
    const cardStyles = {
        backgroundColor: "pink",
        color: "purple",
        width: "300px",
        padding: "20px",
        borderRadius: "10px",
        boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)",
        margin: "auto", // Centers the card horizontally
        textAlign: "center"
    };
    const inputStyles = {
        marginBottom: "10px",
        paddingTop: "5px",
        width: "100%",
        borderRadius: "5px",
        border: "1px solid #ddd"
    };
    const buttonStyles = {
        backgroundColor: "purple",
        color: "white",
        padding: "10px",
        border: "none",
        borderRadius: "5px",
        cursor: "pointer",
        width: "100%",
        fontWeight: "bold"
    };    
    const bodyStyle = {
            marginTop: "50px"
    };
    return( 
        <body style={bodyStyle}>
            <div style={cardStyles}>
                <h1>Login</h1>
                <form>
                <label>Username</label>
                <input type="text" placeholder="Set a Username" style={inputStyles} />
                <label>Email(FCCU)</label>
                <input type="email" placeholder="Enter your Email" style={inputStyles} />
                <label>Password</label>
                <input type="password" placeholder="Set a Password" style={inputStyles} />
                <button style={buttonStyles}>Login</button>
                </form>
            </div>
        </body>
    );
};
export default Login