import React, { useState, useEffect } from "react";
import {useParams, useLocation } from "react-router-dom";
import "./index.css";
import {Row,Col,Button,Input, InputNumber, Radio, Select, message} from 'antd';
import { CloseCircleOutlined } from '@ant-design/icons';
import { addRecipe, getRecipeById, updateRecipe } from '../../api/recipe';
import UploadFile from "./uploadFile";
const { TextArea } = Input;
const Recipe = () => {
  /* init components */
  const { Option } = Select;
  const {recipeId} = useParams();
  const location = useLocation();

  /* data */
  const [recipe, setRecipe] = useState({
    name: "",
    picture: "",
    meal_type: "Breakfast",
    ingredients: [],
    method: [],
    create_time: "",
  });
  const mealTypeOptions = [
    { label: "Breakfast", value: "Breakfast" },
    { label: "Lunch", value: "Lunch" },
    { label: "Dinner", value: "Dinner" },
    // { label: "Other", value: "other" },
  ];
  const [ingredient, setIngredient] = useState({
    ingredient_num: 0,
    ingredient_unit: "g",
    ingredient_name: "",
  });
  const [ingredients, setIngredients] = useState([]);
  const unitOptions = ["g", "tbsp", "clove", "cloves", "tsp", "ml", "head", " "];
  const [method, setMethod] = useState({
    method_step: 1,
    method_step_content: "SETP",
    method_content: "",
    method_photo: "",
    method_photo_file_name: "",
  });
  const [methods, setMethods] = useState([]);

  /* hooks */
  useEffect(() => {
    const pathname = location.pathname;
    const isEdit = pathname.match('/edit')
    if(isEdit && recipeId) {
      getRecipeById(recipeId).then((res) => {
        if(res.status === 200) {
          const data = res.data.data;
          setRecipe({
            recipe_id: recipeId,
            name: data.recipe_name,
            picture: data.recipe_picture,
            meal_type: data.meal_type,
            create_time: data.create_time,
            contributor: data.contributor,
          });
          setIngredients(data.ingredients);
          setMethods(data.methods);
        }
    }, (err) => {
        message.error("Get Recipe Detail Failed!");
    })
    }
    
  }, [recipeId, location.pathname])
  /* function */
  function onNameChange(name) {
    setRecipe({
      ...recipe,
      name: name,
    });
  }

  function handleFiles(photo) {
    setRecipe({
      ...recipe,
      picture: photo.base64,
    });
  }

  function onMealtypeSelect(e) {
    setRecipe({
      ...recipe,
      meal_type: e.target.value,
    });
  }

  function addIngredients() {
    // add key
    setIngredients([...ingredients, ingredient]);
    setIngredient({
      ingredient_num: 0,
      ingredient_unit: "g",
      ingredient_name: "",
    });
  }

  function onIngredientNumberChange(value) {
    setIngredient({
      ...ingredient,
      ingredient_num: value,
    });
  }

  function handleSelectChange(value) {
    setIngredient({
      ...ingredient,
      ingredient_unit: value,
    });
  }

  function onIngredientNameChange(value) {
    setIngredient({
      ...ingredient,
      ingredient_name: value,
    });
  }

  function removeIngredients(index) {
    const list = ingredients;
    setIngredients(list.filter((item, i) => i !== index));
  }

  function addMethod() {
    const index = methods.length + 1;
    method.method_step = index;
    setMethods([...methods, method]);
    setMethod({
      method_content: "",
      method_photo: "",
      method_photo_file_name: "",
    });
  }

  function onMethodContentChange(value) {
    setMethod({
      ...method,
      method_content: value,
    });
  }

  function handleMethodFiles(file) {
    setMethod({
      ...method,
      method_photo: file.base64,
    });
  }

  function removeMethod(index) {
    const list = methods;
    setMethods(list.filter((item, i) => i !== index));
  }

  function onSubmit() {
    const time = new Date().toJSON().slice(0, 19).replace("T", " ");
    const data = {
      ...recipe,
      ingredients,
      method: methods,
      create_time: time,
    };
    if(recipeId) {
      updateRecipe(data).then(
        (res) => {
            message.success("Update Recipe Success!");
        },
        (err) => {
          message.error("Update Recipe Failed!");
          return err;
        }
      );
    } else {
      addRecipe(data).then(
        (res) => {
            message.success("Save Recipe Success!");
        },
        (err) => {
          message.error("Save Recipe Failed!");
          return err;
        }
      );
    }
  }

  return (
    <main className="recipe-container">
      <Row>
        <Col span={4}></Col>
        <Col span={16} className="recipe-content-container">
          <p className="title-name">Basic Info</p>
          <section className="recipe-section">
            <div className="info-row">
              <span className="info-title">NAME</span>
            </div>
            <div className="info-row">
              <Input
                placeholder="E.g. A Tomato Sandwich"
                value={recipe.name}
                className="info-row-input"
                onChange={(e) => {
                  onNameChange(e.target.value);
                }}
              />
            </div>
            <div className="info-row">
              <span className="info-title">PHOTO</span>
            </div>
            <div className="info-row">
              <UploadFile onFileChange={handleFiles} previewFile={recipe.picture}></UploadFile>
            </div>
            <div className="info-row">
              <span className="info-title">CHOOSE A MEAL-TYPE</span>
            </div>
            <div className="info-row">
              <Radio.Group
                options={mealTypeOptions}
                onChange={onMealtypeSelect}
                value={recipe.meal_type}
              />
            </div>
          </section>

          <p className="title-name">Add Ingredients</p>
          <section className="recipe-section">
            <Row className="info-row">
              <Col span={6}>AMOUNT</Col>
              <Col span={12}>UNIT</Col>
              <Col span={6}>INGREDIENT</Col>
            </Row>
            <Row className="info-row">
              <Col span={6}>
                <InputNumber
                  value={ingredient.ingredient_num}
                  min="0"
                  onChange={onIngredientNumberChange}
                />
              </Col>
              <Col span={12}>
                <Select
                  onChange={handleSelectChange}
                  style={{ width: "120px" }}
                  defaultValue="g"
                >
                  {unitOptions.map((unit) => (
                    <Option key={unit}>{unit}</Option>
                  ))}
                </Select>
              </Col>
              <Col span={6}>
                <Input
                  placeholder="Add ingredients,e.g. flour"
                  value={ingredient.ingredient_name}
                  onChange={(e) => {
                    onIngredientNameChange(e.target.value);
                  }}
                />
              </Col>
            </Row>
            <Row className="info-row">
              <Col span={6} offset={18}>
                <Button type="primary" onClick={addIngredients}>
                  Add to Your List
                </Button>
              </Col>
            </Row>
            {ingredients.map((item, index) => (
              <Row className="info-row" key={index}>
                <Col span={6}>{item.ingredient_num}</Col>
                <Col span={6}>{item.ingredient_unit}</Col>
                <Col span={6}>{item.ingredient_name}</Col>
                <Col span={6}>
                  <Button
                    icon={<CloseCircleOutlined />}
                    onClick={() => {
                      removeIngredients(index);
                    }}
                  ></Button>
                </Col>
              </Row>
            ))}
          </section>

          <p className="title-name">Add Steps</p>
          <section className="recipe-section">
            <div className="info-row flex-col">
              <span className="info-title">Step{methods.length + 1}</span>
              <span className="info-description">STEP DESCRIPTION</span>
              <TextArea
                rows={4}
                placeholder="Add method description"
                className="input-default"
                value={method.method_content}
                onChange={(e) => {
                  onMethodContentChange(e.target.value);
                }}
              />
              <span className="info-title margin-col">ADD ONE PHOTO</span>
              <UploadFile onFileChange={handleMethodFiles}></UploadFile>
            </div>
            <Row className="info-row">
              <Col span={6} offset={18}>
                <Button type="primary" onClick={addMethod}>
                  Add New Step
                </Button>
              </Col>
            </Row>
            {methods.map((item, index) => (
              <Row className="info-row" key={index}>
                <Col span={6}>Step{index + 1}</Col>
                <Col span={6}>
                  <p title={item.method_content}>{item.method_content}</p>
                </Col>
                <Col span={6}>
                  {item.method_photo ? (
                    <img
                      src={item.method_photo}
                      alt="img"
                      className="method-photo"
                    />
                  ) : (
                    ""
                  )}
                </Col>
                <Col span={6}>
                  <Button
                    icon={<CloseCircleOutlined />}
                    onClick={() => {
                      removeMethod(index);
                    }}
                  ></Button>
                </Col>
              </Row>
            ))}
          </section>

          <div className="recipe-add">
            <Button type="primary" onClick={onSubmit}>
              Submit Recipe
            </Button>
          </div>
        </Col>
        <Col span={4}></Col>
      </Row>
    </main>
  );
};

export default Recipe;
