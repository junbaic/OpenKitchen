import { MoreOutlined  } from '@ant-design/icons';
import { Dropdown, Menu, Space, message } from 'antd';
import React from 'react';
import { Link } from "react-router-dom";
import { deleteRecipe } from "../../../../api/recipe";

const DropdownMenu = (props) => {
  const handleMenuClick = e => {
    if(e.key === '1') {
      deleteRecipe(props.recipeId).then(
        (res) => {
          message.success("Delete Recipe Success!");
          props.callbackAfterDelete();
        },
        (err) => {
          message.error("Delete Recipe Failed!");
        }
      );
    }
  };

  const menu = (
    <Menu
      onClick={handleMenuClick}
      items={[
        {
          label: (
            <Link to={`/recipe/edit/${props.recipeId}`}>Edit recipe</Link>
          ),
          key: "0",
        },
        {
          label: 'Delete recipe',
          key: "1",
        },
      ]}
      style={{ fontFamily: "TT commons" }}
    />
  );

  return (
    <Dropdown overlay={menu} trigger={['click']} className="menu">
      <a onClick={(e) => e.preventDefault()}>
        <Space>
          <MoreOutlined style={{fontSize:'15px'}}/>
        </Space>
      </a>
    </Dropdown>
  )
};

export default DropdownMenu;