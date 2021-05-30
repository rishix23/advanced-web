import React from 'react';
import { useForm } from 'react-hook-form';
import './Createcv.css';

function Createcv() {
  const { register, handleSubmit, formState: { errors } } = useForm();

  const onSubmit = (formData) => {
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData)
    };
    fetch('http://localhost:5006/CVTemplate1', requestOptions)
      .then(response => {
        response.blob().then(blob => {
          let url = window.URL.createObjectURL(blob);
          let a = document.createElement('a');
          a.href = url;
          a.download = 'cv.doc';
          a.click();
        });
      });
  }

  return (
    <div className='createcv-main-wrapper'>
      <h3 className="createcv-main-title">Create your CV</h3>
      <p className='createcv-pageinfo'>Fill out the form and recieve a free personalised CV!</p>
      <div className='createcv-wrapper'>
        <form onSubmit={handleSubmit(onSubmit)}>
          <label>Your contact information</label>
          <input type="text" placeholder="Address" {...register('address', { required: "This is required!" })} />
          {errors.address && <p>{errors.address.message}</p>}
          <input type="text" placeholder="Telephone" {...register('telephone', { required: "This is required!" })} />
          {errors.telephone && <p>{errors.telephone.message}</p>}
          <input type="text" placeholder="Email" {...register('email', { required: "This is required!" })} />
          {errors.email && <p>{errors.email.message}</p>}
          <label>Your profile information</label>
          <input type="text" placeholder="Full name" {...register('fullname', { required: "This is required!" })} />
          {errors.fullname && <p>{errors.fullname.message}</p>}
          <textarea type="text" placeholder="Write a short paragraph explaining your key strengths, max 250 characters!" {...register('strengths', { required: "This is required!", maxLength: { value: 250, message: "Max length 250 characters!" } })}>
          </textarea>
          {errors.strengths && <p>{errors.strengths.message}</p>}
          <label>Work experience</label>
          <div className='createcv-workexp-wrapper'>
            <input type="text" id="workexprience-company-first" placeholder="Company" {...register('workexp[0].company', { required: "This is required!" })} />
            {errors.workexp && <p>{errors.workexp[0].company.message}</p>}
            <input type="text" id="workexprience-period-first" placeholder="Period" {...register('workexp[0].period', { required: "This is required!" })} />
            {errors.workexp && <p>{errors.workexp[0].period.message}</p>}
          </div>
          <textarea type="text" placeholder="Work experience description, max 250 characters!" {...register('workexp[0].description', { required: "This is required!", maxLength: { value: 250, message: "Max length 250 characters!" } })}>
          </textarea>
          {errors.workexp && <p>{errors.workexp[0].description.message}</p>}
          <div className='createcv-workexp-wrapper'>
            <input type="text" id="workexprience-company-second" placeholder="Company" {...register('workexp[1].company', { required: "This is required!" })} />
            {errors.workexp && <p>{errors.workexp[1].company.message}</p>}
            <input type="text" id="workexprience-period-second" placeholder="Period" {...register('workexp[1].period', { required: "This is required!" })} />
            {errors.workexp && <p>{errors.workexp[1].period.message}</p>}
          </div>
          <textarea type="text" placeholder="Work experience description, max 250 characters!" {...register('workexp[1].description', { required: "This is required!", maxLength: { value: 250, message: "Max length 250 characters!" } })}>
          </textarea>
          {errors.workexp && <p>{errors.workexp[1].description.message}</p>}
          <div className='createcv-workexp-wrapper'>
            <input type="text" id="workexprience-company-third" placeholder="Company" {...register('workexp[2].company', { required: "This is required!" })} />
            {errors.workexp && <p>{errors.workexp[2].company.message}</p>}
            <input type="text" id="workexprience-period-third" placeholder="Period" {...register('workexp[2].period', { required: "This is required!" })} />
            {errors.workexp && <p>{errors.workexp[2].period.message}</p>}
          </div>
          <textarea type="text" placeholder="Work experience description, max 250 characters!" {...register('workexp[2].description', { required: "This is required!", maxLength: { value: 250, message: "Max length 250 characters!" } })}>
          </textarea>
          {errors.workexp && <p>{errors.workexp[2].description.message}</p>}
          <label>Education</label>
          <div className='createcv-edu-wrapper'>
            <input type="text" id="edu-school-first" placeholder="School" {...register('education[0].school', { required: "This is required!" })} />
            {errors.education && <p>{errors.education[0].school.message}</p>}
            <input type="text" id="edu-period-first" placeholder="Period" {...register('education[0].period', { required: "This is required!" })} />
            {errors.education && <p>{errors.education[0].period.message}</p>}
          </div>
          <textarea type="text" placeholder="Education description, max 250 characters!" {...register('education[0].description', { required: "This is required!", maxLength: { value: 250, message: "Max length 250 characters!" } })}>
          </textarea>
          {errors.education && <p>{errors.education[0].description.message}</p>}
          <div className='createcv-edu-wrapper'>
            <input type="text" id="edu-school-second" placeholder="School" {...register('education[1].school', { required: "This is required!" })} />
            {errors.education && <p>{errors.education[1].school.message}</p>}
            <input type="text" id="edu-period-second" placeholder="Period" {...register('education[1].period', { required: "This is required!" })} />
            {errors.education && <p>{errors.education[1].period.message}</p>}
          </div>
          <textarea type="text" placeholder="Education description, max 250 characters!" {...register('education[1].description', { required: "This is required!", maxLength: { value: 250, message: "Max length 250 characters!" } })}>
          </textarea>
          {errors.education && <p>{errors.education[1].description.message}</p>}
          <div className='createcv-edu-wrapper'>
            <input type="text" id="edu-school-third" placeholder="School" {...register('education[2].school', { required: "This is required!" })} />
            {errors.education && <p>{errors.education[2].school.message}</p>}
            <input type="text" id="edu-period-third" placeholder="Period" {...register('education[2].period', { required: "This is required!" })} />
            {errors.education && <p>{errors.education[2].period.message}</p>}
          </div>
          <textarea type="text" placeholder="Education description, max 250 characters!" {...register('education[2].description', { required: "This is required!", maxLength: { value: 250, message: "Max length 250 characters!" } })}>
          </textarea>
          {errors.education && <p>{errors.education[2].description.message}</p>}
          <label>Voulnteering</label>
          <div className='createcv-volunteering-wrapper'>
            <input type="text" id="volunteering-org-first" placeholder="Organisation" {...register('volunteering[0].org', { required: "This is required!" })} />
            {errors.volunteering && <p>{errors.volunteering[0].org.message}</p>}
            <input type="text" id="volunteering-period-first" placeholder="Period" {...register('volunteering[0].period', { required: "This is required!" })} />
            {errors.volunteering && <p>{errors.volunteering[0].period.message}</p>}
          </div>
          <textarea type="text" placeholder="Education description, max 250 characters!" {...register('volunteering[0].description', { required: "This is required!", maxLength: { value: 250, message: "Max length 250 characters!" } })}>
          </textarea>
          {errors.volunteering && <p>{errors.volunteering[0].description.message}</p>}
          <div className='createcv-volunteering-wrapper'>
            <input type="text" id="volunteering-org-first" placeholder="Organisation" {...register('volunteering[1].org', { required: "This is required!" })} />
            {errors.volunteering && <p>{errors.volunteering[1].org.message}</p>}
            <input type="text" id="volunteering-period-first" placeholder="Period" {...register('volunteering[1].period', { required: "This is required!" })} />
            {errors.volunteering && <p>{errors.volunteering[1].period.message}</p>}
          </div>
          <textarea type="text" placeholder="Education description, max 250 characters!" {...register('volunteering[1].description', { required: "This is required!", maxLength: { value: 250, message: "Max length 250 characters!" } })}>
          </textarea>
          {errors.volunteering && <p>{errors.volunteering[1].description.message}</p>}
          <label>Skills</label>
          <textarea type="text" placeholder="List your key technical skills, max 250 characters!" {...register('skills', { required: "This is required!", maxLength: { value: 250, message: "Max length 250 characters!" } })}>
          </textarea>
          {errors.skills && <p>{errors.skills.message}</p>}
          <label>Proffessional qualifications</label>
          <div className='createcv-profqual-wrapper'>
            <input type="text" id="profqual-qual" placeholder="Qualification" {...register('profqual.qual', { required: "This is required!" })} />
            {errors.profqual && <p>{errors.profqual.qual.message}</p>}
            <input type="text" id="profqual-date" placeholder="Date" {...register('profqual.date', { required: "This is required!" })} />
            {errors.profqual && <p>{errors.profqual.date.message}</p>}
          </div>
          <input type="submit" />
        </form>
      </div>
    </div>
  );
}

export default Createcv;
