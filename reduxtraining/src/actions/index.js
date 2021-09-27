export const increment = (by = 1) => {
  return { type: "INCREMENT", payload: by };
};

export const decrement = () => {
  return { type: "DECREMENT" };
};
