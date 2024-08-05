import { useState } from "react";
import BlogList from "./BlogList";

const Home = () => {
    // reactive values. Whenever the variable name changes, it will re render the templates
    // const [name, setName] = useState('melvin');
    // const [age, setAge] = useState(25);

    // const handleClick = (e) => {
    //     /* adding e to get the event logged in */
    //     console.log(e);

    //     setName('audrey');
    //     setAge(35);
    // }

    // // const handleClickAgain = (name, e) => {
    // //     console.log("Hello " + name, e)
    // // }
    
    // return (
    //     <div className="home">
    //         <h2>Homepage</h2>
    //         <p>{ name } is { age } yo</p>
    //         <button onClick={handleClick}>Click me</button>
    //     </div>
    // );

    const [blogs, setBlogs] = useState([
        { title: 'My new website', body: 'lorem ipsum...', author: 'mario', id: 1 },
        { title: 'Welcome party!', body: 'lorem ipsum...', author: 'yoshi', id: 2 },
        { title: 'Web dev top tips', body: 'lorem ipsum...', author: 'mario', id: 3 }
    ]);

    return (
        // <div className="home">
        //     {/* cycle through blogs with map js function */}
        //     {blogs.map((blog) => (
        //         <div className="blog-preview" key={blog.id}>
        //             <h2>{blog.title}</h2>
        //             <p>Written by {blog.author}  </p>
        //         </div>
        //     ))}
        // </div>

        <div className="home">
            <BlogList blogs={blogs} title="All Blogs" />
            <BlogList blogs={blogs.filter((blog) => blog.author === 'mario')} title="Mario's blogs" />
        </div>
    )
}

export default Home;