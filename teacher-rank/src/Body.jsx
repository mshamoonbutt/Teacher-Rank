function Body(){
    const styles = {
        textAlign : "center",
        marginTop : "110px",
        // paddingBottom : "100%",
        color : "pink"
    }
    const footer = {
        color : "pink",
        paddingTop: "150px",
        paddingBottom : "20px",
        textAlign : "center"
    }
    return(
        <>
        <body style={styles}>
            <h1>
                Welcome to Teacher Rank
            </h1>
            <p>A place where you can find the best teacher for your course</p>
        </body>
        <footer style={footer}> 
            <p>A project by M.Abdulrehman Goraya, Ahmed Hamza and Shamoon Butt</p>
        </footer>
        </>
    );
};
export default Body