import agentAPI from "./agent";
import { dashboardData } from "../data/dashboardData";

// Temporary until backend is ready
export const investigate = async (query) => {
  console.log("Investigation Query:", query);

  await new Promise((resolve) => setTimeout(resolve, 3500));

  return dashboardData;
};

/*

replace the code with something like  

export const investigate = async (query) => {
    const { data } = await agentAPI.post("/investigate", {
        query,
    });

    return data;
};

*/