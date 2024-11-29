import { Link } from "react-router-dom";

const Register_page = () => {
  return (
    <section className="flex justify-center items-center h-screen">
      <div className="flex flex-col gap-4">
        <h1 className="text-2xl font-medium uppercase py-6">Registration</h1>
        <div>
          <form>
            <div>
              <label className="input input-bordered flex items-center gap-2">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 16 16"
                  fill="currentColor"
                  className="h-4 w-4 opacity-70"
                >
                  <path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6ZM12.735 14c.618 0 1.093-.561.872-1.139a6.002 6.002 0 0 0-11.215 0c-.22.578.254 1.139.872 1.139h9.47Z" />
                </svg>
                <input type="text" className="grow" placeholder="Username" />
              </label>
            </div>
            <div>
              <p>Email</p>
            </div>
            <div>
              <p>Password</p>
            </div>
          </form>
          <div>
            <p>Already have an account?</p>
            <Link to="/login">
              <button>Login</button>
            </Link>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Register_page;
