import axios from 'axios';

<<<<<<< HEAD
<<<<<<< HEAD
const baseURL = 'http://192.168.0.87:8000/MiGanado_app'; // Ajusta la URL a la de tu servidor
=======
const baseURL = 'http://192.168.0.10:8000/miGanado'; // Ajusta la URL a la de tu servidor
>>>>>>> main
=======
const baseURL = 'http://192.168.0.209:8000/miGanado'; // Ajusta la URL a la de tu servidor
>>>>>>> e3e072929b99ec86afb1f3d32668aaa3292942ad

const registerUser = async (userData) => {
  try {
    const response = await axios.post(`${baseURL}/usuarios/`, userData);
    return response.data;
  } catch (error) {
    if (error.response) {
      console.error('Error al registrar el usuario:', error.response.data);
    } else {
      console.error('Error al registrar el usuario:', error.message);
    }
    throw error;
  }
};

const loginUser = async (email, password) => {
  try {
    const response = await axios.post(`${baseURL}/login/`, { email, password });
    return response.data;
  } catch (error) {
    if (error.response) {
      console.error('Error al iniciar sesión - Respuesta del servidor:', error.response.data);
    } else if (error.request) {
      console.error('Error al iniciar sesión - No se recibió respuesta:', error.request);
    } else {
      console.error('Error al iniciar sesión:', error.message);
    }
    throw error;
  }
};


const getUserLotes = async (userId) => {
  try {
    const response = await axios.get(`${baseURL}/usuarios/${userId}/`);
    return response.data.lotes;
  } catch (error) {
    if (error.response) {
      console.error('Error al obtener los lotes del usuario:', error.response.data);
    } else {
      console.error('Error al obtener los lotes del usuario:', error.message);
    }
    throw error;
  }
};

const getUserNotificaciones = async (userId) => {
  try {
    const response = await axios.get(`${baseURL}/usuarios/${userId}/`); 
    return response.data.notificaciones;
  } catch (error) {
    if (error.response) {
      console.error('Error al obtener los lotes del usuario:', error.response.data);
    } else {
      console.error('Error al obtener los lotes del usuario:', error.message);
    }
    throw error;
  }
};




const createSangrado = async ({ numero_lote, numero_animal, numero_tubo, fecha, userId }) => {
  try {
    const response = await axios.post(`${baseURL}/sangrados/`, { numero_lote, numero_animal, numero_tubo, fecha, userId });
    return response.data;
  } catch (error) {
    if (error.response) {
      console.error('Error al guardar los datos de sangrado:', error.response.data);
    } else {
      console.error('Error al guardar los datos de sangrado:', error.message);
    }
    throw error;
  }
};
const createTacto = async ({ numero_lote, numero_animal, prenada, fecha, userId }) => {
  try {
    const response = await axios.post(`${baseURL}/tactos/`, { numero_lote, numero_animal, prenada, fecha, userId });
    return response.data;
  } catch (error) {
    if (error.response) {
      console.error('Error al guardar los datos del tacto:', error.response.data);
    } else {
      console.error('Error al guardar los datos del tacto:', error.message);
    }
    throw error;
  }
};








export { baseURL, registerUser, loginUser, getUserLotes, getUserNotificaciones,createSangrado,createTacto};