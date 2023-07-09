import React, {useState} from 'react';
import {EditCategory, ICategoryProps} from "./interfaces";
import axios from "axios";
import {Simulate} from "react-dom/test-utils";
import input = Simulate.input;

const Category = ({value, key, setReload}: ICategoryProps) => {


  const [editCategory, setEditCategory] = useState(false)

  let edit_category: EditCategory = {
    name: '',
    slug: '',
    parent: 0,
    file: null
  }

  const deleteCategory = (slug: string) => {
    axios.delete(`http://localhost:8000/category/${slug}/delete`)
      .then((response) => {
        alert('Удалено')
        setReload(prev => !prev)
      })
  }

  const updateCategory = () => {

    let formData = new FormData()
    if (edit_category.file) {
      formData.append('file', edit_category.file, edit_category.file.filename)
    }
    formData.append('category', JSON.stringify({name: edit_category.name, slug: edit_category.slug, parent: edit_category.parent}))

    axios.patch(`http://localhost:8000/category/${value.slug}/update`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
        'accept': 'application/json'
      }
    })
      .then((response) => {
        alert('Добавлено')
        setEditCategory(false)
        setReload(prev => !prev)
      })
      .catch((response) => {
        alert(response.status)
      })
  }

  const clickInput = (event: any) => {
    event.stopPropagation()
  }

  return <tr className={`border ` + (key%2===0 && 'bg-gray-300')} onClick={() => setEditCategory(prev => !prev)}>
          <td className={`text-center`}>{value.id}</td>
          <td className={`text-center`}>
            {!editCategory ?
              value.name :
              <input className={`border`} type="text" onClick={clickInput} onChange={
                (event) => {
                  edit_category.name = event.target.value
                }
              }/>
            }
          </td>
          <td className={`text-center`}>
            {!editCategory ? value.slug : <input className={`border`} type="text" onClick={clickInput} onChange={
              (event) => {
                edit_category.slug = event.target.value
              }
            }/>}
          </td>
          <td className={`text-center`}>
            {!editCategory ? value.parent : <input className={`border`} type="number" onClick={clickInput} onChange={
              (event) => {
                edit_category.parent = parseInt(event.target.value)
              }
            }/>}
          </td>
          <td className={`text-center`}>{value.parent_category}</td>
          <td className={`text-center`}>
            {!editCategory ? value.image : <input className={`border`} type="file" onClick={clickInput} onChange={
              (event) => {
                if (event.target.files)
                edit_category.file = event.target.files[0]
              }
            }/>}
          </td>
          <td className={`border text-center`} onClick={() => {
            !editCategory ?
              deleteCategory(value.slug) :
                updateCategory()
          }}>
            {!editCategory ? '-' : '+'}
          </td>
        </tr>
  
};

export default Category;