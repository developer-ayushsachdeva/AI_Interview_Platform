// import axios from "axios";

// const BASE_URL = "http://127.0.0.1:8000/interview";

// export const startInterviewAPI = async () => {
//     try {
//         const response = await axios.get(`${BASE_URL}/start`);
//         return response.data;
//     } catch (error) {
//         console.error("Error:", error);
//         return null;
//     }
// };

// export const submitAPI = async (payload) => {
//   try {
//     const response = await axios.post(`${BASE_URL}/submit`, payload);
//     return response.data;
//   } catch (error) {
//     console.error("Error: ", error);
//   }

//   return null;
// };

// export const reportAPI = async (sessionId) => {
//   try {
//     const response = await axios.get(`${BASE_URL}/report/${sessionId}`);
//     return response.data;
//   } catch (error) {
//     console.error("Error: ", error);
//   }

//   return null;
// };

// export const endInterviewAPI = async (sessionId) => {
//   try {
//     const response = await axios.put(`${BASE_URL}/end/${sessionId}`);
//     return response.data;
//   } catch (error) {
//     console.error("Error: ", error);
//   }

//   return null;
// };



import axios from "axios";

const BASE_URL = "https://ai-interview-platform-g39c.onrender.com/interview";

// Generate interview questions and create a session
export const generateQuestionsAPI = async (formData) => {
  try {
    const response = await axios.post(
      `${BASE_URL}/generate-question`,
      formData
    );

    return response.data;
  } catch (error) {
    console.error("Error generating questions:", error);
    throw error;
  }
};

// Start interview using the generated session
export const startInterviewAPI = async (sessionId) => {
  try {
    const response = await axios.get(
      `${BASE_URL}/start/${sessionId}`
    );

    return response.data;
  } catch (error) {
    console.error("Error starting interview:", error);
    throw error;
  }
};

// Submit candidate answer
export const submitAPI = async (payload) => {
  try {
    const response = await axios.post(
      `${BASE_URL}/submit`,
      payload
    );

    return response.data;
  } catch (error) {
    console.error("Error submitting answer:", error);
    throw error;
  }
};

// End interview
export const endInterviewAPI = async (sessionId) => {
  try {
    const response = await axios.put(
      `${BASE_URL}/end/${sessionId}`
    );

    return response.data;
  } catch (error) {
    console.error("Error ending interview:", error);
    throw error;
  }
};

// Generate interview report
export const reportAPI = async (sessionId) => {
  try {
    const response = await axios.get(
      `${BASE_URL}/report/${sessionId}`
    );

    return response.data;
  } catch (error) {
    console.error("Error generating report:", error);
    throw error;
  }
};
