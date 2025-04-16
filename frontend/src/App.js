import React, { useState } from "react";
import axios from "axios";
import "./App.css";

const App = () => {
  const initialFormData = {
    no_of_dependents: "",
    education: "",
    self_employed: "",
    income_annum: "",
    loan_amount: "",
    loan_term: "",
    cibil_score: "",
    residential_assets_value: "",
    commercial_assets_value: "",
    luxury_assets_value: "",
    bank_asset_value: "",
  };

  const [formData, setFormData] = useState(initialFormData);
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setPrediction(null);
    setError("");

    const data = new FormData();
    for (const key in formData) {
      data.append(key, formData[key]);
    }

    try {
      const res = await axios.post("http://127.0.0.1:5000/predict", data);
      setPrediction(res.data.prediction);
    } catch (err) {
      console.error(err);
      setError("Failed to get prediction. Try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="diabetes-form-container">
      <h1 className="form-title">Loan Approval Prediction</h1>
      <form className="diabetes-form" onSubmit={handleSubmit}>
        {Object.entries(formData).map(([key, value]) => (
          <div className="form-field" key={key}>
            <label className="field-label">{key.replace(/_/g, " ")}:</label>
            {key === "education" ? (
              <select
                name={key}
                value={value}
                onChange={handleChange}
                className="field-input"
              >
                <option value="">Select</option>
                <option value="Graduate">Graduate</option>
                <option value="Not Graduate">Not Graduate</option>
              </select>
            ) : key === "self_employed" ? (
              <select
                name={key}
                value={value}
                onChange={handleChange}
                className="field-input"
              >
                <option value="">Select</option>
                <option value="Yes">Yes</option>
                <option value="No">No</option>
              </select>
            ) : (
              <input
                className="field-input"
                type="number"
                name={key}
                value={value}
                onChange={handleChange}
              />
            )}
          </div>
        ))}
        <button className="submit-button" type="submit" disabled={loading}>
          {loading ? "Predicting..." : "Submit"}
        </button>
      </form>

      {prediction && (
        <div
          className={`result ${
            prediction === "Approved" ? "approved" : "rejected"
          }`}
        >
          <strong>Prediction:</strong> {prediction}
        </div>
      )}

      {error && <div className="error-message">{error}</div>}
    </div>
  );
};

export default App;
