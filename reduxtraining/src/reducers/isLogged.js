const loggedInitialState = {
  isLogged: false,
};

const loggedReducer = (state = loggedInitialState, action) => {
  switch (action.type) {
    case "SIGN_IN":
      return {
        ...state,
        isLogged: true,
      };
    case "SIGN_OUT":
      return {
        ...state,
        isLogged: false,
      };
    default:
      return state;
  }
};

export default loggedReducer;
