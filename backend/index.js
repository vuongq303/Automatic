const express = require("express");
const mongoose = require("mongoose");

const app = express();
app.use(express.json());

const urlConnectMongodb =
  "mongodb+srv://hoangquan:WXtVprHBhv2skTNq@cluster0.m5rmad6.mongodb.net/Automatic";

mongoose
  .connect(urlConnectMongodb)
  .then(() => console.log("Connected"))
  .catch((err) => console.log("Error connect: ", err));

app.get("/", (_, res) => {
  res.send("...");
});

const groupSchema = new mongoose.Schema({
  username: String,
  group: String,
});

const groupModel = mongoose.model("groups", groupSchema);

const userSchema = new mongoose.Schema({
  username: String,
  password: String,
  status: {
    default: true,
    type: Boolean,
  },
});
const userModel = mongoose.model("users", userSchema);

app.post("/new-group", async function (req, res) {
  const { username, group } = req.body;

  try {
    const result = await groupModel.insertMany({
      username: username,
      group: group,
    });

    if (result.length > 0) {
      res.status(200).json({ response: "Added new group", type: true });
      return;
    }
    res.status(200).json({ response: "Added new group failed", type: false });
  } catch (error) {
    console.log(error);
  }
});

app.post("/new-user", async function (req, res) {
  const { username, password } = req.body;

  try {
    const result = await userModel.insertMany({
      username: username,
      password: password,
    });
    if (result.length > 0) {
      res.status(200).json({ response: "Added new user", type: true });
      return;
    }
    res.status(200).json({ response: "Added new user failed", type: false });
  } catch (error) {
    console.log(error);
  }
});

app.post("/verify-user", async function (req, res) {
  const { username, password } = req.body;
  try {
    const result = await userModel.find({
      username: username,
      password: password,
    });

    if (result.length > 0) {
      res.status(200).json({ response: "Verify new user", type: true });
      return;
    }
    res.status(200).json({ response: "Verify new user failed", type: false });
  } catch (error) {
    console.log(error);
  }
});

app.get("/groups", async function (req, res) {
  const { username } = req.params;
  try {
    const result = await groupModel.find({ username: username });
    res.status(200).send({ response: result });
  } catch (error) {
    console.log(error);
  }
});
