function Siginup(){
    return(
        <body>
            <div>
                <h1>Sigin Up</h1>
                <form>
                    <label>Username</label>
                    <input type="text" placeholder="Set a Username"></input>
                    <label>Email(FCCU)</label>
                    <input type="email" placeholder="Enter your Email"></input>
                    <label>Password</label>
                    <input type="password" placeholder="Set a Username"></input>
                    <label>Screen Shot of Transcript</label>
                    <input type="file" accept="image/*"></input>
                    <button>Submit</button>
                </form>
            </div>
        </body>
    );
};
export default Siginup