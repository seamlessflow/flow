import React, { useState, ChangeEvent, FormEvent } from "react";
import LabeledInput from "../LabeledInput/LabeledInput";
import axios from 'axios'
import "./SignUp.scss";

interface SignUpProps {
  buttonUrl: string;
}

const SignUp = ({ buttonUrl }: SignUpProps): JSX.Element => {
  const [email, setemail] = useState<string>("");
  const handleEmailChange = (event: ChangeEvent<HTMLInputElement>) => {
    setemail(event.target.value);
  };
  const checkEmail = (email: string) => {
    const expression: RegExp = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    const result: boolean = expression.test(email); // true

    return result;
  };

  // Define the URL where your Sling Servlet is mapped
  // const servletUrl = 'tsproject/components/customForm';

  // const submitForm = (formData: FormData) => {
  //   axios
  //     .post(servletUrl, formData)
  //     .then((response) => {
  //       // Handle a successful form submission
  //       console.log('Form submitted successfully');
  //     })
  //     .catch((error) => {
  //       // Handle errors
  //       console.error('Error submitting form:', error);
  //     });
  // };


  const handleSubmit = (event: FormEvent) => {
    event.preventDefault();
    // Assuming you have a form element with an "id" attribute, e.g., <form id="myForm">...</form>
    const formElement = document.getElementById('myForm') as HTMLFormElement | null;
    console.log(formElement)
    // if (formElement) {
    //   // The form element exists, you can now create FormData from it
    //   const formData = new FormData(formElement);

    //   // Your FormData is ready for use
    //   console.log("Form is submitted!");
    //   submitForm(formData)

    // }

    // Page redirect
    if (typeof buttonUrl == "string") {
      if (checkEmail(email)) {
        console.log(email);


        window.location.href = buttonUrl;
      } else {
        console.log("Email inválido");
      }
    }
  };
  return (
    <div className="formdiv">
      <form onSubmit={handleSubmit}>
        <div className="formbody">
          <LabeledInput
            label="Full Name*"
            type="text"
            placeholder="Name"
            onChange={() => { }}
            required
          />
          {
            <LabeledInput
              label="Email*"
              required
              type="email"
              placeholder="foo@bar.com"
              onChange={handleEmailChange}
            />
          }
          <LabeledInput
            label="Phone"
            type="tel"
            placeholder="(83) 00000-0000"
            required={false}
            onChange={() => { }}
          />
          <LabeledInput
            label="Password*"
            type="password"
            placeholder="Enter your password"
            onChange={() => { }}
            required
          />
          <LabeledInput
            label="Birthday*"
            type="date"
            placeholder="dd/mm/yyyy"
            onChange={() => { }}
            required
          />
        </div>
        <div className="formfooter">
          <div>
            <input
              className="checkbox"
              type="checkbox"
              required={true}
              id="terms"
              value="false"
            />
            <label>I accept the terms and privacy</label>
          </div>
          <button type="submit">Register</button>
        </div>
      </form>
    </div>
  );
};

export default SignUp;
