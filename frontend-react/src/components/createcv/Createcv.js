import React from 'react';
import { useForm } from 'react-hook-form';
import './Createcv.css';

function Createcv() {
  const { register, handleSubmit, formState: { errors } } = useForm();

  const onSubmit = (data) => {
    console.log(data)
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
            <input type="text" id="workexprience-company" placeholder="Company" {...register('workexp.company', { required: "This is required!" })} />
            {errors.workexp && <p>{errors.workexp.company.message}</p>}
            <input type="text" id="workexprience-period" placeholder="Period" {...register('workexp.period', { required: "This is required!" })} />
            {errors.workexp && <p>{errors.workexp.period.message}</p>}
          </div>
          <label>Education</label>
          <div className='createcv-edu-wrapper'>
            <input type="text" id="edu-school" placeholder="School" {...register('education.school', { required: "This is required!" })} />
            {errors.education && <p>{errors.education.school.message}</p>}
            <input type="text" id="edu-period" placeholder="Period" {...register('education.period', { required: "This is required!" })} />
            {errors.education && <p>{errors.education.period.message}</p>}
          </div>
          <label>Voulnteering</label>
          <div className='createcv-volunteering-wrapper'>
            <input type="text" id="volunteering-org" placeholder="Organisation" {...register('volunteering.org', { required: "This is required!" })} />
            {errors.volunteering && <p>{errors.volunteering.org.message}</p>}
            <input type="text" id="volunteering-period" placeholder="Period" {...register('volunteering.period', { required: "This is required!" })} />
            {errors.volunteering && <p>{errors.volunteering.period.message}</p>}
          </div>
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