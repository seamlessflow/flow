import React from "react";
import "./LabeledInput.scss";

interface LabeledInputProps {
  label?: string;
  type: string;
  placeholder: string;
  required: boolean;
  onChange: Function;
}

const LabeledInput = ({
  label,
  type = "text",
  placeholder,
  required = false,
  onChange,
}: LabeledInputProps): JSX.Element => {
  return (
    <div className="main">
      <label className="terms">{label}</label>
      <input
        type={type}
        placeholder={placeholder}
        required={required}
        onChange={(e) => onChange(e)}
      />
    </div>
  );
};

export default LabeledInput;
