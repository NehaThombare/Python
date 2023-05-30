using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BallMovement : MonoBehaviour
{
    public float Speed;
        void FixedUpdate(){
            float HorizontalMovement=Input.GetAxis("Horizontal");
            float VerticalMovement=Input.GetAxis("Vertical");

            Vector3 MoveBall=new 
        Vector3(HorizontalMovement,0,VerticalMovement);
        
        gameObject.transform.GetComponent<Rigidbody>().AddForce(MoveBall*Speed);
    }
}
