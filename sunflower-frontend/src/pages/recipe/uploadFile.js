import React, { useState, useEffect } from "react";
import { Modal, Upload } from "antd";
import { PlusOutlined  } from "@ant-design/icons";
// import ReactFileReader from "react-file-reader";
import './uploadFile.css'

const UploadFile = (props) => {
  const [fileList, setFileList] = useState([]);
  const [previewOpen, setPreviewOpen] = useState(false);
  const [previewImage, setPreviewImage] = useState("");
  const [previewTitle, setPreviewTitle] = useState("");

  useEffect(() => {
    if (props.previewFile) {
      setFileList([{
        uid: "-1",
        name: "preview.png",
        status: "done",
        url: props.previewFile,
      }]);
    }
  }, [props.previewFile]);

  const getBase64 = (file) =>
    new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = () => resolve(reader.result);
      reader.onerror = (error) => reject(error);
  });

  function setFileAfterImg(base64) {
    props.onFileChange({ base64 });
  }

  const handleCancel = () => setPreviewOpen(false);
  const handlePreview = async (file) => {
    if (!file.url && !file.preview) {
      file.preview = await getBase64(file.originFileObj);
    }
    setPreviewImage(file.url || file.preview);
    setPreviewOpen(true);
    setPreviewTitle(
      file.name || file.url.substring(file.url.lastIndexOf("/") + 1)
    );
  };
  const handleChange = async ({ fileList: newFileList }) => {
    setFileList(newFileList);
    const file = newFileList[0];
    if(!file.url && !file.preview) {
      const base64Code = await getBase64(newFileList[0].originFileObj);
      setFileAfterImg(base64Code);
    } else {
       props.onFileChange({ base64: '' });
    }
  }

  function beforeUpload(file) {
    return false;
  }

   const uploadButton = (
     <div>
       <PlusOutlined />
       <div
         style={{
           marginTop: 8,
         }}
       >
         Upload
       </div>
     </div>
   );

  return (
    <main className="upload-file">
      <Upload
        listType="picture-card"
        fileList={fileList}
        maxCount={1}
        onPreview={handlePreview}
        onChange={handleChange}
        beforeUpload={beforeUpload}
      >
        {fileList.length >= 2 ? null : uploadButton}
      </Upload>
      <div className="image-content">
        <span className="image-title">Upload A Photo</span>
        <span className="image-text">photo must be jpg or png type and size should be less than 4Mb</span>
      </div>
      <Modal
        open={previewOpen}
        title={previewTitle}
        footer={null}
        onCancel={handleCancel}
      >
        <img
          alt="example"
          style={{
            width: "100%",
          }}
          src={previewImage}
        />
      </Modal>
    </main>
  );
};
export default UploadFile;